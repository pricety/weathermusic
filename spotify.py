""" spotify api calls and client credential authorization"""
import os
import json
import base64
import random
import requests
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")



""" function getting playlist from
api and client credential flow """
def get_playlist(weather_code): # pylint: disable = too-many-locals, missing-function-docstring

    # Step 1 - Authorization
    url = "https://accounts.spotify.com/api/token"
    headers = {}
    data = {}

    # Encode as Base64
    message = f"{client_id}:{client_secret}"
    messageBytes = message.encode('ascii') # pylint: disable = invalid-name
    base64Bytes = base64.b64encode(messageBytes) # pylint: disable = invalid-name
    base64Message = base64Bytes.decode('ascii') # pylint: disable = invalid-name


    headers['Authorization'] = f"Basic {base64Message}"
    data['grant_type'] = "client_credentials"

    r = requests.post(url, headers=headers, data=data) # pylint: disable = invalid-name

    token = r.json()['access_token']



    playlist_details = {}
    rain = {389, 386, 359, 356, 353, 314, 311, 308, 305, 302, 299, 296, 293, 284, 281, 266, 263, 260, 248, 200, 185, 176, 143} # pylint: disable = line-too-long
    snow = {395, 392, 377, 374, 371, 368, 365, 362, 350, 338, 335, 332, 329, 326, 323, 320, 317, 230, 227, 182, 179} # pylint: disable = line-too-long
    sunny ={122, 119, 116, 113}

    SUNNY_PHRASES = [ # pylint: disable = invalid-name
                "it's hot outside",
                "cool off with this playlist"
        ]

    RAIN_PHRASES = [ # pylint: disable = invalid-name
            "it's pouring outside",
            "stay dry and vibe with this playlist"
        ]

    SNOW_PHRASES = [ # pylint: disable = invalid-name
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


    playlistUrl = f"https://api.spotify.com/v1/playlists/{playlist_id}" # pylint: disable = invalid-name




    headers = {
        "Authorization": f"Bearer {token}"
    }

    res = requests.get(playlistUrl, headers=headers)

    print(json.dumps(res.json(), indent=2))


    data = res.json()

    playlist_details = {
        "playlist_id": data["id"],
        "playlist_name": data["name"],
        "link": data["external_urls"]["spotify"],
        "phrase": phrase
    }


    return playlist_details
