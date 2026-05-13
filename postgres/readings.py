import os
import psycopg2
from psycopg2.extras import RealDictCursor


def get_readings(page, limit=25):
    offset = (page - 1) * limit

    with psycopg2.connect(database=os.getenv('PG_DB'),
                          user=os.getenv('PG_USER'),
                          password=os.getenv('PG_PWD')) as conn:

        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(
                'SELECT readings.id, v.vendor_name, passenger_count, trip_distance, rc.code, store_and_fwd_flag, z.zone_name AS pu_location, z.zone_name AS do_location, pt.payment_type, fare_amount, extra, mta_tax, tip_amount, tolls_amount, improvement_surcharge, total_amount, congestion_surcharge, "Airport_fee", tpep_pickup_datetime AS pickup_time, tpep_dropoff_datetime AS dropoff_time'
                ' FROM readings'
                ' INNER JOIN vendors AS v ON v."VendorID" = yellow_trips."VendorID"'
                ' INNER JOIN rate_codes AS rc ON rc."RatecodeID" = yellow_trips."RatecodeID"'
                ' INNER JOIN zones AS z ON z."LocationID" = "PULocationID" AND z."LocationID" = "DOLocationID"'
                ' INNER JOIN payment_types AS pt ON pt.id = yellow_trips.payment_type'
                ' LIMIT %s OFFSET %s', (limit, offset))

            trips = cursor.fetchall()
            return trips