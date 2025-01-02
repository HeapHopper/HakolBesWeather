import pandas as pd
from datetime import datetime
from weather_forecast.forecast_factory import *

def current_weather_presenter(lat,lon):
    return new_current_weather(lat,lon).dict()

def hourly_data_presenter(lat,lon,days=7):
    hourly = new_hourly_forecast(lat,lon,days)
    hourly_data = {"datetime": pd.date_range(start=hourly.time[0], end=hourly.time[-1], freq='h'),
                   "temperature": hourly.temperature, "humidity": hourly.humidity, "rain probability": hourly.rain_prob}
    hourly_dataframe = pd.DataFrame(data=hourly_data)
    return hourly_dataframe

def hourly_wind_data_presenter(lat,lon,days=7):
    hourly = new_hourly_forecast(lat,lon,days=7)
    hourly_data = {"datetime": pd.date_range(start=hourly.time[0], end=hourly.time[-1], freq='h'),
                   "wind_speed": hourly.wind_speed, "wind_direction": [parse_wind_direction_util(direction) for direction in hourly.wind_direction]}
    hourly_dataframe = pd.DataFrame(data=hourly_data)
    return hourly_dataframe

def daily_data_presenter(lat,lon,days=7):
    daily = new_daily_forecast(lat, lon, days)
    daily_data = {"Date": [datetime.fromisoformat(dt).date() for dt in daily.time],
                  "Minimum Temperature": [round(temp,3) for temp in daily.min_temp],
                  "Maximum Temperature": [round(temp,3) for temp in daily.max_temp],
                  "Sunrise": [datetime.fromisoformat(dt).time() for dt in daily.sunrise],
                  "Sunset": [datetime.fromisoformat(dt).time() for dt in daily.sunset]}
    daily_dataframe = pd.DataFrame(data=daily_data)
    daily_dataframe.set_index('Date')
    return daily_dataframe


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
        "North", "North-East", "East", "South-East",
        "South", "South-West", "West", "North-West"
    ]

    # There are 8 cardinal directions, so each covers 45 degrees
    index = round(degrees / 45) % 8
    return directions[index]

print(hourly_data_presenter(40.7128,-74.0060))
print(hourly_wind_data_presenter(40.7128,-74.0060))
print(daily_data_presenter(40.7128,-74.0060))

#print(daily_data_presenter(40.7128,-74.0060))