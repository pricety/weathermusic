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

def get_playlist(token, weather_code): 
    playlist_details = {}
    rain = {389, 386, 359, 356, 353, 314, 311, 308, 305, 302, 299, 296, 293, 284, 281, 266, 263, 260, 248, 200, 185, 176, 143}
    snow = {395, 392, 377, 374, 371, 368, 365, 362, 350, 338, 335, 332, 329, 326, 323, 320, 317, 230, 227, 182, 179}
    sunny ={122, 119, 116, 113}

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

    random_sunny = random.choice(SUNNY_PHRASES)
    random_rain = random.choice(RAIN_PHRASES)
    random_snow = random.choice(SNOW_PHRASES)



    if weather_code in sunny:
        playlist_id = "6f5nTqNFhK4yl17V8Nj95k"
        phrase = random_sunny
    elif weather_code in rain:
        playlist_id = "5v6c0Iby3qiUnsHlf0CIYn"
        phrase = random_rain
    elif weather_code in snow:
        playlist_id = "2mOE7f9OQ4OkCc4qKdDfWq"
        phrase = random_snow


    SPOTIFY_GET_PLAYLIST_URL = f"https://api.spotify.com/v1/playlists/{playlist_id}" # pylint: disable = invalid-name

    response = requests.get(
            SPOTIFY_GET_PLAYLIST_URL,
            headers={
                "Authorization": f"Bearer {token}"
            }
        )
    json_resp = response.json()
    print(json_resp)
    playlist_details = {
        "playlist_id": json_resp["id"],
        "playlist_name": json_resp["name"],
        "link": json_resp["external_urls"]["spotify"],
        "phrase": phrase
    }

    return playlist_details
