from pydantic import BaseModel

class CurrentWeather(BaseModel):
    time: str | None
    temperature: float | None
    humidity: int | None
    rain_prob: float | None
    wind_speed: float | None
    wind_direction: int | None

    sunrise: str | None
    sunset: str | None
    weather_code: int | None
    uv_index: float | None

class HourlyForecast(BaseModel):
    latitude:   float
    longitude:  float

    time: list(str) | None
    temperature: list(float) | None
    humidity: list(int) | None
    rain_prob: list(float) | None
    wind_speed: list(float) | None
    wind_direction: list(int) | None

class DailyForecast(BaseModel):
    latitude:   float
    longitude:  float

    time: list(str) | None
    weather_codes: list(int) | None
    sunrise: list(str) | None
    sunset: list(str) | None
    uv_index: list(float) | None
