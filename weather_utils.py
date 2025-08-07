import requests
from dotenv import load_dotenv
import os #new import for environment variable loading
load_dotenv() #.env is added to the project root

api_key= os.getenv("open_weather_api_key")

def fetch_weather(city):
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }
    except requests.exceptions.HTTPError:
        return None
