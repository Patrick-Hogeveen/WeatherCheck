DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;

CREATE TABLE city (
  city_id INTEGER PRIMARY KEY AUTOINCREMENT,
  city_name TEXT NOT NULL,
  state_name TEXT,
  country_code TEXT NOT NULL,
  UNIQUE (city_id, state_name, country_code)
);

CREATE TABLE query (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  city_id INTEGER NOT NULL,
  queried_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  success BOOLEAN NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (city_id) REFERENCES city (city_id)
);