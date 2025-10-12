from fastapi import FastAPI
import requests
import os

app = FastAPI(title="Gothenburg Weather API", version="1.0.0")

API_KEY = os.getenv("OPENWEATHER_API_KEY")
if not API_KEY:
    raise ValueError("Please set the OPENWEATHER_API_KEY environment variable")

BASE_URL = "https://api.openweathermap.org/data/2.5"
CITY = "Gothenburg"
UNITS = "metric"


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/weather")
def get_current_weather():
    url = f"{BASE_URL}/weather?q={CITY}&appid={API_KEY}&units={UNITS}"
    response = requests.get(url)
    data = response.json()
    if response.status_code != 200:
        return {"error": data.get("message", "Unable to fetch weather data")}
    return {
        "city": CITY,
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"]
    }


@app.get("/forecast")
def get_weather_forecast():
    url = f"{BASE_URL}/forecast?q={CITY}&appid={API_KEY}&units={UNITS}"
    response = requests.get(url)
    data = response.json()
    if response.status_code != 200:
        return {"error": data.get("message", "Unable to fetch forecast data")}
    forecasts = []
    for item in data["list"][:5]:
        forecasts.append({
            "datetime": item["dt_txt"],
            "temperature": item["main"]["temp"],
            "description": item["weather"][0]["description"]
        })
    return {
        "city": CITY,
        "forecast": forecasts
    }
