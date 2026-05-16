import os
import psycopg2
from psycopg2.extras import RealDictCursor


def get_readings_hourly_chosen_day(date_day):
    with psycopg2.connect(database=os.getenv('PG_DB'),
                          user=os.getenv('PG_USER'),
                          password=os.getenv('PG_PWD')) as conn:

        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            _query = 'SELECT date_hour, value, units, parameter FROM readings'
            'WHERE date_day = %s GROUP BY date_hour, value, units, parameter'
            'ORDER BY date_hour;'
            cursor.execute(_query, (date_day,))

            readings_hourly = cursor.fetchall()
            return readings_hourly


def get_number_of_all_readings():
    with psycopg2.connect(database=os.getenv('PG_DB'),
                          user=os.getenv('PG_USER'),
                          password=os.getenv('PG_PWD')) as conn:

        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            _query = 'SELECT COUNT(id) AS number_of_readings FROM readings;'
            cursor.execute(_query)

            readings_count = cursor.fetchall()
            return readings_count