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

#Showing all readings hourly on a chosen day
@app.route('/api/readings/<date_day>/all_readings/hourly', methods=['GET'])
def get_readings_hourly_chosen_day(date_day):

    readings_hourly = postgres.readings.get_readings_hourly_chosen_day(date_day)
    return jsonify(readings_hourly)

#Showing the number of all readings
@app.route('/api/readings/count', methods=['GET'])
def get_number_of_all_readings():

    readings_count = postgres.readings.get_number_of_all_readings()
    return jsonify(readings_count)


#Showing daily average values of a chosen sensor using sensors_id
# Sensor_ids: o3 = 26979, pm10 = 11415, no2 = 11420, so2 = 27064, pm25 = 11401
@app.route('/api/readings/sensor/<sensors_id>/avg_values/daily', methods=['GET'])
def get_avg_values_daily_chosen_sensor_sensorsId(sensors_id):

    avg_values_daily = postgres.readings.get_avg_values_daily_chosen_sensor_sensorsId(sensors_id)
    return jsonify(avg_values_daily)



#Showing daily average values of a chosen sensor using parameter
# Parameters: o3 = 26979, pm10 = 11415, no2 = 11420, so2 = 27064, pm25 = 11401
@app.route('/api/readings/parameter/<parameter>/avg_values/daily', methods=['GET'])
def get_avg_values_daily_chosen_sensor_parameter(parameter):

    avg_values_daily = postgres.readings.get_avg_values_daily_chosen_sensor_parameter(parameter)
    return jsonify(avg_values_daily)


if __name__ == '__main__':
    app.run(debug=True)
    #debug=True, port=6000)