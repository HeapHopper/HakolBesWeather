from weather_forecast.forecast import *
from weather_forecast.forecast_api import *

def new_current_weather():
    pass

def new_hourly_forecast(latitude, longitude, days=7):
    data = get_hourly_forcast(latitude,longitude,days)
    return HourlyForecast(latitude=latitude,
                              longitude=longitude,
                              days=days,
                              time=data["time"],
                              temperature=data["temperature_2m"],
                              humidity=data["relative_humidity_2m"],
                              rain_prob=data["rain"],
                              wind_speed=data["wind_speed_10m"],
                              wind_direction=data["wind_direction_10m"])

def new_daily_forecast(latitude, longitude, days=7):
    pass

print(new_hourly_forecast(31.7788242,35.2257626))