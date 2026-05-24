import os
import psycopg2
from psycopg2.extras import RealDictCursor


def get_readings_hourly_chosen_day(date_day):
    with psycopg2.connect(database=os.getenv('PG_DB'),
                          user=os.getenv('PG_USER'),
                          password=os.getenv('PG_PWD')) as conn:

        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            _query = ('SELECT date_hour, date_month, value, units, parameter FROM readings '
            'WHERE date_day = %s GROUP BY date_hour, date_month, value, units, parameter '
            'ORDER BY parameter;')
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


# Daily avg values: choosing sensor by sensors_id
def get_avg_values_daily_chosen_sensor_sensorsId(sensors_id):
    with psycopg2.connect(database=os.getenv('PG_DB'),
                          user=os.getenv('PG_USER'),
                          password=os.getenv('PG_PWD')) as conn:

        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            _query = ('SELECT date_day, parameter, AVG(value) AS avg_value FROM readings '
                      'WHERE sensors_id = %s GROUP BY date_day, parameter '
                      'ORDER BY date_day;')
            cursor.execute(_query, (sensors_id,))

            avg_values_daily = cursor.fetchall()
            return avg_values_daily


# Daily avg values: choosing sensor by parameter
def get_avg_values_daily_chosen_sensor_parameter(parameter):
    with psycopg2.connect(database=os.getenv('PG_DB'),
                          user=os.getenv('PG_USER'),
                          password=os.getenv('PG_PWD')) as conn:

        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            _query = ('SELECT date_day, parameter, AVG(value) AS avg_value, sensors_id FROM readings '
                      'WHERE parameter = %s GROUP BY date_day, parameter, sensors_id '
                      'ORDER BY date_day;')
            cursor.execute(_query, (parameter,))

            avg_values_daily = cursor.fetchall()
            return avg_values_daily


def get_avg_values():
    with psycopg2.connect(database=os.getenv('PG_DB'),
                          user=os.getenv('PG_USER'),
                          password=os.getenv('PG_PWD')) as conn:

        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            _query = ('SELECT parameter, AVG(value) AS avg_value FROM readings '
                      'GROUP BY parameter;')
            cursor.execute(_query)
            avg_values = cursor.fetchall()
            return avg_values