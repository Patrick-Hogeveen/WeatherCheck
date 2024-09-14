INSERT INTO city (city_name, state_name, country_code)
VALUES
  ('Toronto', '', 'ISO 3166-2:CA'),
  ('New York', 'US-NY', 'ISO 3166-2:US');

INSERT INTO query (city_id, queried_at, success, body)
VALUES
  ('2', '2024-09-13 21:10:58.000000', True, '{
    "coord": {
        "lon": -74.006,
        "lat": 40.7143
    },
    "weather": [
        {
            "id": 800,
            "main": "Clear",
            "description": "clear sky",
            "icon": "01n"
        }
    ],
    "base": "stations",
    "main": {
        "temp": 293.74,
        "feels_like": 294,
        "temp_min": 291.54,
        "temp_max": 294.8,
        "pressure": 1023,
        "humidity": 82,
        "sea_level": 1023,
        "grnd_level": 1022
    },
    "visibility": 10000,
    "wind": {
        "speed": 1.54,
        "deg": 250
    },
    "clouds": {
        "all": 0
    },
    "dt": 1726285993,
    "sys": {
        "type": 1,
        "id": 4610,
        "country": "US",
        "sunrise": 1726223716,
        "sunset": 1726268913
    },
    "timezone": -14400,
    "id": 5128581,
    "name": "New York",
    "cod": 200
}'),
("1", '2024-09-13 21:10:58.000000', False, ""),
('2', '2024-09-12 21:10:58.000000', True, '{
    "coord": {
        "lon": -74.006,
        "lat": 40.7143
    },
    "weather": [
        {
            "id": 800,
            "main": "Clear",
            "description": "clear sky",
            "icon": "01n"
        }
    ],
    "base": "stations",
    "main": {
        "temp": 293.74,
        "feels_like": 294,
        "temp_min": 291.54,
        "temp_max": 294.8,
        "pressure": 1023,
        "humidity": 82,
        "sea_level": 1023,
        "grnd_level": 1022
    },
    "visibility": 10000,
    "wind": {
        "speed": 1.54,
        "deg": 250
    },
    "clouds": {
        "all": 0
    },
    "dt": 1726285993,
    "sys": {
        "type": 1,
        "id": 4610,
        "country": "US",
        "sunrise": 1726223716,
        "sunset": 1726268913
    },
    "timezone": -14400,
    "id": 5128581,
    "name": "New York",
    "cod": 200
}');