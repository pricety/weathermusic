import os 
import requests
import random
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
redirect_uri = f"{os.getenv('URL')}/callback"

def my_Profile(token):
    dict = {}
    SPOTIFY_GET_ME = 'https://api.spotify.com/v1/me' # pylint: disable = invalid-name

    response = requests.get(
            SPOTIFY_GET_ME,
            headers={
                "Authorization": f"Bearer {token}"
            }
        )

    json_resp = response.json()
    if "email" in json_resp:
        dict["email"] = json_resp["email"] 
    else:
        dict["email"]= None
    if "country" in json_resp:
        dict["country"] = json_resp["country"]
    else:
        dict["country"] = None
    if "display_name" in json_resp:
        dict["display_name"] = json_resp["display_name"]
    else: 
        dict["display_name"] = None
    print(json_resp)
    print(json_resp["images"])
    if "images" in json_resp:
        if len(json_resp["images"]) != 0:
            dict["images"] = json_resp["images"][0]["url"]
        else: 
            dict["images"] = None
    else:
        dict["images"] = None
    return dict

def get_playlist(token):
    playlist_details = {}

    SUNNY_PHRASES = [
            "it's hot outside",
            "cool off with this playlist"
    ]

    RAIN_PHRASES = [
        "it's pouring outside",
        "stay dry and vibe with this playlist"
    ]

    SNOW_PHRASES = [
        "baby, it's cold outside",
        "warm up with this",
        "let it snow"
    ]

    WEATHER_DESCRIPTIONS = [
        "sunny",
        "rain",
        "snow"
    ]

    description = random.choice(WEATHER_DESCRIPTIONS)
    random_sunny = random.choice(SUNNY_PHRASES)
    random_rain = random.choice(RAIN_PHRASES)
    random_snow = random.choice(SNOW_PHRASES)


    if description == "sunny":
        playlist_id = "6f5nTqNFhK4yl17V8Nj95k"
        phrase = random_sunny
    elif description == "rain":
        playlist_id = "5v6c0Iby3qiUnsHlf0CIYn"
        phrase = random_rain
    else:
        playlist_id = "2mOE7f9OQ4OkCc4qKdDfWq"
        phrase = random_snow


    SPOTIFY_GET_PLAYLIST_URL = f"https://api.spotify.com/v1/{playlist_id}" # pylint: disable = invalid-name

    response = requests.get(
            SPOTIFY_GET_PLAYLIST_URL,
            headers={
                "Authorization": f"Bearer {token}"
            }
        )
    json_resp = response.json()

    track_details["playlist_id"] = json_resp['id']
    track_details["playlist_name"] = json_resp['name']

    track_details["link"] = json_resp['external_urls']['spotify']


    return (track_details, phrase)
