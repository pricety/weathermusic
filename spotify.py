import random



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

def get_playlist_info(description):

  if description == "sunny":
    playlist_id = "6f5nTqNFhK4yl17V8Nj95k"
    phrase = random_sunny
    return (phrase, playlist_id)

  if description == "rain":
    playlist_id = "5v6c0Iby3qiUnsHlf0CIYn"
    phrase = random_rain
    return (phrase, playlist_id)

  if description == "snow":
    playlist_id = "2mOE7f9OQ4OkCc4qKdDfWq"
    phrase = random_snow
    return (phrase, playlist_id)
