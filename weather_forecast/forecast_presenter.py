import pandas as pd
from weather_forecast.forecast_factory import *

def current_weather_presenter(lat,lon):
    return new_current_weather(lat,lon).dict()

def hourly_data_presenter(lat,lon,days=7):
    hourly = new_hourly_forecast(lat,lon,days)
    hourly_data = {"datetime": pd.date_range(start=hourly.time[0], end=hourly.time[-1], freq='h'),
                   "temperature": hourly.temperature, "humidity": hourly.humidity, "rain probability": hourly.rain_prob}
    hourly_dataframe = pd.DataFrame(data=hourly_data)
    return hourly_dataframe

def hourly_wind_data_presenter(lat,lon):
    pass

def daily_data_presenter(lat,lon):
    pass
def parse_weather_code_util(code):
    wmo_descriptions = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Depositing rime fog",
        51: "Drizzle: Light",
        53: "Drizzle: Moderate",
        55: "Drizzle: Dense intensity",
        56: "Freezing drizzle: Light",
        57: "Freezing drizzle: Dense intensity",
        61: "Rain: Slight",
        63: "Rain: Moderate",
        65: "Rain: Heavy intensity",
        66: "Freezing rain: Light",
        67: "Freezing rain: Heavy intensity",
        71: "Snowfall: Slight",
        73: "Snowfall: Moderate",
        75: "Snowfall: Heavy intensity",
        77: "Snow grains",
        80: "Rain showers: Slight",
        81: "Rain showers: Moderate",
        82: "Rain showers: Violent",
        85: "Snow showers: Slight",
        86: "Snow showers: Heavy",
        95: "Thunderstorm: Slight or moderate",
        96: "Thunderstorm with slight hail",
        99: "Thunderstorm with heavy hail",
    }
    return wmo_descriptions.get(code,"N/A")

def parse_wind_direction_util(degrees):
    if degrees < 0 or degrees > 360:
        return "Invalid direction"

    directions = [
        "North", "North-Northeast", "Northeast", "East-Northeast",
        "East", "East-Southeast", "Southeast", "South-Southeast",
        "South", "South-Southwest", "Southwest", "West-Southwest",
        "West", "West-Northwest", "Northwest", "North-Northwest", "North"
    ]

    # There are 16 cardinal directions, so each covers 22.5 degrees
    index = round(degrees / 22.5) % 16
    return directions[index]

print(hourly_data_presenter(40.7128,-74.0060))