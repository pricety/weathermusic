import requests, json
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


zipcode = 30308
zip_url = (
    "https://www.zipcodeapi.com/rest/"
    + os.getenv("ZIPKEY")
    + "/info.json/"
    + str(zipcode)
    + "/degrees"
)
zip_request = requests.get(zip_url)
zip_response = zip_request.json()
for key, value in zip_response.items():
    if key == "city":
        city_name = value
print("cityname: ", city_name)

# ---------------------------------------------------------------------------------------------------------------

base_url = "http://api.openweathermap.org/data/2.5/weather?zip="
complete_url = (
    base_url + str(zipcode) + "&units=imperial" + "&appid=" + os.getenv("WEATHERKEY")
)


weather_response = requests.get(complete_url)


x = weather_response.json()

# "404", means city not found
if x["cod"] != "404":

    y = x["main"]

    current_temperature = y["temp"]

    z = x["weather"]

    weather_description = z[0]["description"]

    print(
        " Temperature = "
        + str(current_temperature)
        + "\n description = "
        + str(weather_description)
    )

else:
    print(" City Not Found ")
