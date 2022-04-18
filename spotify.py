import os 
import requests
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

def get_track(token):
    track_details = {}
    SPOTIFY_GET_TRACK_URL = 'https://api.spotify.com/v1/tracks/11dFghVXANMlKmJXsNCbNl' # pylint: disable = invalid-name

    response = requests.get(
            SPOTIFY_GET_TRACK_URL,
            headers={
                "Authorization": f"Bearer {token}"
            }
        )
    json_resp = response.json()

    track_details["track_id"] = json_resp['album']['id']
    track_details["track_name"] = json_resp['name']
    artists = list(json_resp['artists'])

    track_details["link"] = json_resp['external_urls']['spotify']

    track_details["artist_names"] = ', '.join([artist['name'] for artist in artists])

    return track_details