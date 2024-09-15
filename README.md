# WeatherCheck
A simple flask wrapper for checking the local weather in a city. Currently uses <a href="https://openweathermap.org/">OpenWeatherMap</a>. Currently serves 2 endpoints weather/:id and weather/history displaying the weather in a city given its id in the database and a history of the last 5 successful queries made respectively. 

```
Steps:
Clone
Create venv
pip install -r .\requirements.txt
Create .env file containing your openweathermap API key in the weather directory
flask --app weather init-db
flask --app weather run --host=0.0.0.0
```

# Structure
Project includes a weather directory where the factory and app logic are contained a well as a test directory for testing them using pytest. 

# Design
The database schema was designed simply, at first the city table included a column for weather but that was removed as the query table can simply be queried for the last mention of a given city if its previous state of weather is needed. In the end queries are stored with their city_id, timestamp, if they were successful, and what was returned (empty if the API call failed). The city table is simply a cities Id, name, state (if in the United States) and ISO country code. This was done as it worked best with the chosen weather API and also to avoid the problem of quering cities with the same name in different countries. 

Optimizations could be made ie. replacing the database for something like postgres and using a caching db for frquently requested destinations. A few html files are included and were planned to be implemented so the endpoint could serve html based requests but that has not been fully implemented at this time. The endpoint currently only logs failed requests to existing cities and not requests to cities that are not supported, it may be prudent to log requests for cities not contained in the database.



