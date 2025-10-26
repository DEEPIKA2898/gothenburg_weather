from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import requests, os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Gothenburg Weather Dashboard")

templates = Jinja2Templates(directory="app/templates")

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5"
CITY = "Gothenburg"
UNITS = "metric"

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    weather_url = f"{BASE_URL}/weather?q={CITY}&appid={API_KEY}&units={UNITS}"
    forecast_url = f"{BASE_URL}/forecast?q={CITY}&appid={API_KEY}&units={UNITS}"
    
    weather = requests.get(weather_url).json()
    forecast = requests.get(forecast_url).json()
    
    if "main" not in weather:
        return templates.TemplateResponse("index.html", {"request": request, "error": "Weather data unavailable"})
    
    forecasts = [
        {
            "datetime": item["dt_txt"],
            "temp": item["main"]["temp"],
            "desc": item["weather"][0]["description"].capitalize()
        }
        for item in forecast["list"][:5]
    ]
    
    return templates.TemplateResponse("index.html", {
        "request": request,
        "city": CITY,
        "temp": weather["main"]["temp"],
        "desc": weather["weather"][0]["description"].capitalize(),
        "humidity": weather["main"]["humidity"],
        "wind": weather["wind"]["speed"],
        "forecasts": forecasts
    })
