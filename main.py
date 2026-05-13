from flask import Flask, jsonify
from dotenv import load_dotenv

import postgres.countries
import postgres.timezones
import postgres.localities
import postgres.locations
import postgres.sensors
import postgres.readings

app = Flask(__name__)

load_dotenv()

# Routehandlers here:

# Showing countries
@app.route('/api/countries', methods=['GET'])
def get_countries():
    countries = postgres.countries.get_countries()
    return jsonify(countries)

# Showing timezones
@app.route('/api/timezones', methods=['GET'])
def get_timezones():
    timezones = postgres.timezones.get_timezones()
    return jsonify(timezones)

#Showing localities
@app.route('/api/localities', methods=['GET'])
def get_localities():
    localities = postgres.localities.get_localities()
    return jsonify(localities)

#Showing locations
@app.route('/api/locations', methods=['GET'])
def get_locations():
    locations = postgres.locations.get_locations()
    return jsonify(locations)

#Showing sensors
@app.route('/api/sensors', methods=['GET'])
def get_sensors():

    sensors = postgres.sensors.get_sensors()
    return jsonify(sensors)


if __name__ == '__main__':
    app.run(debug=True)
    #debug=True, port=6000)