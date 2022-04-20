import requests
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

def weather_info(location, metric_type):
    WEATHER_URL = "http://api.weatherstack.com/current"

    params = {
        "access_key": os.getenv("WEATHER_KEY"),
        "query": location,
        "units": metric_type, #units in fahrenheit, will later add a button to switch between celcius and fahrenheit
    }

    weather_results = requests.get(WEATHER_URL, params)
    weather_data = weather_results.json()
    current_data = weather_data["current"] 
    location_data = weather_data["location"]

    metric = ""
    speed = ""
    if metric_type == "m":
        metric = "C"
        speed = "km/h"
    elif metric_type == "f":
        metric = "F"
        speed = "mi/h"

    weather_details = {
        "temperature": current_data["temperature"],
        "description": str(current_data["weather_descriptions"][0]),
        "weather_code": current_data["weather_code"],
        "wind_speed": current_data["wind_speed"],
        "wind_direction": current_data["wind_dir"],
        "humidity": current_data["humidity"],
        "cloud_cover": current_data["cloudcover"],
        "feels_like": current_data["feelslike"],
        "uv_index": current_data["uv_index"],
        "visibility": current_data["visibility"],
        "metric_type": metric,
        "speed": speed
    }
    
    location_details = {
        "name": location_data["name"],
        "region": location_data["region"],
        "lat": location_data["lat"],
        "lon": location_data["lon"],
    }

    return weather_details, location_details