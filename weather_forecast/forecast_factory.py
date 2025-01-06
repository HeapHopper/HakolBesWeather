from weather_forecast.forecast import *
from weather_forecast.forecast_api import *
from timezone_util.timezone_util import *

def new_current_weather(latitude, longitude):
    # TODO
    timezone_name = location_to_tz_util(float(latitude),float(longitude))
    target_time = get_local_time(timezone_name)
    current = fetch_current_forecast(latitude, longitude,timezone_name)
    return CurrentWeather(latitude=latitude,
                          longitude=longitude,
                          time=current["time"],
                          timezone=timezone_name,
                          localtime=target_time,
                          temperature=current["temperature_2m"],
                          apparent_temperature=current["apparent_temperature"],
                          weather_code=current["weather_code"],
                          humidity=current["relative_humidity_2m"],
                          wind_speed=current["wind_speed_10m"],
                          wind_direction=current["wind_direction_10m"])

def new_hourly_forecast(latitude, longitude, days=7):
    timezone_name = location_to_tz_util(float(latitude),float(longitude))
    data = fetch_hourly_forcast(latitude,longitude,timezone_name,days)
    return HourlyForecast(latitude=latitude,
                          longitude=longitude,
                          days=days,
                          time=data["time"],
                          timezone=timezone_name,
                          temperature=data["temperature_2m"],
                          humidity=data["relative_humidity_2m"],
                          rain_prob=data["rain"],
                          wind_speed=data["wind_speed_10m"],
                          wind_direction=data["wind_direction_10m"])

def new_daily_forecast(latitude, longitude, days=7):
    timezone_name = location_to_tz_util(float(latitude),float(longitude))
    data = fetch_daily_forcast(latitude, longitude, timezone_name,days)
    return DailyForecast(latitude=latitude,
                         longitude=longitude,
                         days=days,
                         time=data["time"],
                         timezone=timezone_name,
                         weather_code=data["weather_code"],
                         min_temp=data["temperature_2m_min"],
                         max_temp=data["temperature_2m_max"],
                         sunrise=data["sunrise"],
                         sunset=data["sunset"])

if __name__=="__main__":
    print(new_hourly_forecast(31.7788242,35.2257626))
    print(new_daily_forecast(31.7788242,35.2257626))
    print(new_current_weather(31.7788242,35.2257626))
