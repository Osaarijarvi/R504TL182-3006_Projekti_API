import os
import psycopg2
from psycopg2.extras import RealDictCursor


def get_sensors():
    with psycopg2.connect(database=os.getenv('PG_DB'),
                          user=os.getenv('PG_USER'),
                          password=os.getenv('PG_PWD')) as conn:

        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            _query = "SELECT * FROM sensors"
            cur.execute(_query)
            sensors = cur.fetchall()
            return sensors