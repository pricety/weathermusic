import os 
import requests
import random
import base64
import json
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")



def get_playlist():

#    GET_TOKEN = 'https://api.spotify.com/api/token'
#    clients = f"{client_id}:{client_secret}"
#    clients = clients.encode("ascii")
#    base64_bytes = base64.b64encode(clients)
#    base64_clients = base64_bytes.decode('ascii')
#  
#    Authorization = {
#        'Authorization': f'Basic{base64_clients}',
#        "Content Type": "application/x-www-form-urlencoded"
#    }
#    grant_type = 'client_credentials'

#    resp = requests.post(
#        GET_TOKEN,
#        grant_type,
#        headers={
#            'Authorization': f'Basic {base64_clients}' + base64_clients.replace('\c',''),
#            "Content Type": "application/x-www-form-urlencoded"
#        }
#    )

#    access_token = resp.text


    # Step 1 - Authorization
    url = "https://accounts.spotify.com/api/token"
    headers = {}
    data = {}

    # Encode as Base64
    message = f"{client_id}:{client_secret}"
    messageBytes = message.encode('ascii')
    base64Bytes = base64.b64encode(messageBytes)
    base64Message = base64Bytes.decode('ascii')


    headers['Authorization'] = f"Basic {base64Message}"
    data['grant_type'] = "client_credentials"

    r = requests.post(url, headers=headers, data=data)

    token = r.json()['access_token']





#    Authorization = {
#        'Authorization': f'Basic{base64_clients}',
#        "Content Type": "application/x-www-form-urlencoded"
#    }
#    grant_type = 'client_credentials'

#    resp = requests.post(
#        GET_TOKEN,
#        grant_type,
#        headers={
#            'Authorization': f'Basic {base64_clients}' + base64_clients.replace('\c',''),
#            "Content Type": "application/x-www-form-urlencoded"
#        }
#    )





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


    playlistUrl = f"https://api.spotify.com/v1/playlists/{playlist_id}" # pylint: disable = invalid-name




    headers = {
        "Authorization": f"Bearer {token}" 
    }

    res = requests.get(playlistUrl, headers=headers)

    print(json.dumps(res.json(), indent=2))

#    parsedData = res.parse(res);

    data = res.json()

    playlist_details = {
        "playlist_id": data["id"],
        "playlist_name": data["name"],
        "link": data["external_urls"]["spotify"],
        "phrase": phrase
    }



#    response = requests.get(
#            SPOTIFY_GET_PLAYLIST_URL,
#            headers={
#                "Authorization": f"Bearer {token}"
#            }
#        )
#    json_resp = res.json()

#    id = data['id']
#    name = data['name']

#    playlist_details["playlist_id"] = json_resp['id']
#    playlist_details["playlist_name"] = json_resp['name']

#    playlist_details["link"] = json_resp['external_urls']['spotify']


    return playlist_details
