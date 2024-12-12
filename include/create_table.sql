CREATE SCHEMA IF NOT EXISTS {{ params.schema }};

CREATE TABLE IF NOT EXISTS {{ params.schema }}.{{ params.table }} (
    date DATE NOT NULL,
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL,
    sunset TIMESTAMPTZ NOT NULL,
    PRIMARY KEY (date, latitude, longitude)
);