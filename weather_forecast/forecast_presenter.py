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

print(hourly_data_presenter(40.7128,-74.0060))