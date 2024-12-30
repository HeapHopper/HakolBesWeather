from weather_forecast.forecast import *
from weather_forecast.forecast_api import *

def new_current_weather(latitude, longitude):
    # TODO
    # This isn't the actual current weather, this is more of a "today" weather
    # extracting the correct data to the current time is to be done...
    hourly = new_hourly_forecast(latitude, longitude,days=1)
    daily= new_daily_forecast(latitude, longitude,days=1)
    print(hourly)
    return CurrentWeather(time=hourly.time[0],
                          temperature=hourly.temperature[0],
                          humidity=hourly.humidity[0],
                          rain_prob=hourly.rain_prob[0],
                          wind_speed=hourly.wind_speed[0],
                          wind_direction=hourly.wind_direction[0],
                          sunrise=daily.sunrise[0],
                          sunset=daily.sunset[0],
                          weather_code=daily.weather_code[0],
                          uv_index=daily.uv_index[0])

def new_hourly_forecast(latitude, longitude, days=7):
    data = fetch_hourly_forcast(latitude,longitude,days)
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
    data = fetch_daily_forcast(latitude, longitude, days)
    return DailyForecast(latitude=latitude,
                         longitude=longitude,
                         days=days,
                         time=data["time"],
                         weather_code=data["weather_code"],
                         sunrise=data["sunrise"],
                         sunset=data["sunset"],
                         uv_index=data["uv_index_max"])

print(new_hourly_forecast(31.7788242,35.2257626))
print(new_daily_forecast(31.7788242,35.2257626))
print(new_current_weather(31.7788242,35.2257626))
