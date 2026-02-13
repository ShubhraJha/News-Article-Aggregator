import requests
import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")
def get_user_location():
    try:
        response = requests.get("http://ip-api.com/json/",timeout=5)
        data = response.json()
        city = data.get("city")
        lat = data.get("lat")
        lon = data.get("lon")
        return city, lat, lon
    except:
        return None, None, None

def get_weather():
    API_KEY = os.getenv("OPENWEATHER_API_KEY")
    city, lat, lon = get_user_location()
    if not lat or not lon or not API_KEY:
        return "Weather unavailable", city
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url, timeout=5)
        data = response.json()
        if response.status_code != 200:
            return "Weather unavailable", city
        temp = data["main"]["temp"]
        description = data["weather"][0]["main"]
        return f"{temp}°C | {description}", city
    except:
        return "Weather unavailable", city

