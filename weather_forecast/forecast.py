from pydantic import BaseModel

class CurrentWeather(BaseModel):
    latitude:   float
    longitude:  float

    time: str | None
    timezone: str | None
    localtime: str | None

    temperature: float | None
    apparent_temperature: float | None
    weather_code: int | None
    humidity: int | None
    wind_speed: float | None
    wind_direction: int | None

class HourlyForecast(BaseModel):
    latitude:   float
    longitude:  float

    days: int
    time: list[str] | None

    temperature: list[float] | None
    humidity: list[int] | None
    rain_prob: list[float] | None
    wind_speed: list[float] | None
    wind_direction: list[int] | None

class DailyForecast(BaseModel):
    latitude:   float
    longitude:  float

    days: int = 7
    time: list[str] | None

    weather_code: list[int] | None
    min_temp: list[float] | None
    max_temp: list[float] | None
    sunrise: list[str] | None
    sunset: list[str] | None
