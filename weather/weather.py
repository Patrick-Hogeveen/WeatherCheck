from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from markupsafe import escape
from weather.db import get_db
import requests, json, functools, os, datetime, time
from dotenv import load_dotenv



load_dotenv()

bp = Blueprint('weather', __name__, url_prefix='/weather')

@bp.route("/", methods=("GET", "POST"))
def home():
    db = get_db()

    error = None
    cities = db.execute(
        'SELECT * FROM city'
    ).fetchall()
    
    returnval = [{"city_id": city['city_id'], "city_name": city['city_name'], "state_name":city['state_name'], "country_code":city['country_code']} for city in cities]

    return returnval

@bp.route('/<int:id>', methods=['GET'])
def check(id):
    db = get_db()
    key = os.getenv('WEATHER_APIKEY')
    error = None
    print(key)
    if key is None:
        error = "Please provide an openweathermap API key"

    
    city = db.execute(
        'SELECT * FROM city WHERE city_id = ?', (id,)
    ).fetchone()
    time = datetime.datetime.now()
    
    if city is None:
        error = "City is unsupported"

    if error is None:
        base_url = "https://api.openweathermap.org/data/2.5/weather?"

        full_url = base_url + "q=" + city['city_name'] +","+city['country_code'] + "&appid=" + os.getenv('WEATHER_APIKEY')
        response = None
        try:

            response = requests.get(full_url)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            
            
            return str(e.args[0])
        
        jsresponse = response.json()
        
        store = json.dumps(jsresponse)
        if jsresponse['cod'] != "404":
            y = jsresponse["main"]

            curr_temp = y["temp"]
            curr_pressure = y["pressure"]
            curr_humid = y["humidity"]

            weather = jsresponse["weather"]

            description = weather[0]["description"]

            

            try:
                db.execute(
                    "INSERT INTO query (city_id, queried_at, success, body) VALUES (?, ?, ?, ?)",
                    (id, time, True, store)
                )
                db.commit()
            except db.IntegrityError:
                error = f"Inserting data error"
            else:
                return {"city_name": city["city_name"], "temperature":curr_temp, "pressure":curr_pressure, "humidity":curr_humid, "description":description}
        else:
            db.execute(
                    "INSERT INTO query (city_id, queried_at, success, body) VALUES (?, ?, ?, ?)",
                    (id, time, False, "")
                )
            return "Weather API is down"

    return error

@bp.route("/history", methods=['GET'])
def history():
    db = get_db()

    error = None

    history = db.execute(
        'SELECT * FROM query WHERE success == True  ORDER BY queried_at DESC LIMIT 5'
    ).fetchall()
    names = []
    returnval = []
    
    
    for query in history:
        city = db.execute(
            'SELECT * FROM city WHERE city_id = ?',
            (query['city_id'],)
        ).fetchone()
        weather = json.loads(query['body'])
        y = weather["main"]

        curr_temp = y["temp"]
        curr_pressure = y["pressure"]
        curr_humid = y["humidity"]

        weather = weather["weather"]

        description = weather[0]["description"]
        
        queryval = {"city_name":city['city_name'], "time":query["queried_at"], "summary":{"temperature":curr_temp, "pressure":curr_pressure, "humidity":curr_humid, "description":description}}
        
        returnval.append(queryval)

    return returnval






###
@bp.route("/city", methods=('GET','POST'))
def register():
    if request.method == 'POST':
        cityname = request.form['name']
        statecode = request.form['state']
        countrycode = request.form['country']
        db = get_db()
        error=None

        if not cityname:
            error = 'City name is required'
        elif not statecode:
            statecode = ""
        elif not countrycode:
            errpr = 'Country code is required'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO city (city_name, state_name, country_code) VALUES (?, ?, ?)",
                    (cityname, statecode, countrycode),
                )
                db.commit()

            except db.IntegrityError:
                error = f"City already exists"
            else:
                return redirect(url_for("weather.home"))

        flash(error)

    return render_template('register_city.html')


