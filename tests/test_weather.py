import pytest
from flask import g, session
from weather.db import get_db
import json


@pytest.mark.parametrize(('city_id', 'message'), (
    ('10',b"City is unsupported"),
))
def test_city(client, city_id, message):
    assert client.get('/weather/'+city_id).data == message

def test_history(client, app):
    
    value = value = b'[{"city_name":"New York","summary":{"description":"clear sky","humidity":82,"pressure":1023,"temperature":293.74},"time":"Fri, 13 Sep 2024 21:10:58 GMT"},{"city_name":"New York","summary":{"description":"clear sky","humidity":82,"pressure":1023,"temperature":293.74},"time":"Thu, 12 Sep 2024 21:10:58 GMT"}]\n'
    print(value)
    print(client.get('/weather/history').data)
    
    assert client.get('/weather/history').data == value
   
    #Maybe test city registration endpoint?