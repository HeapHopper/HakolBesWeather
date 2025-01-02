import requests

OPEN_METEO_URL = "https://api.open-meteo.com/v1/forecast"

def fetch_current_forecast(lat,lon):
    # API parameters
    params = {
        "latitude": lat,
        "longitude": lon,
        "current": ["temperature_2m", "relative_humidity_2m", "apparent_temperature", "weather_code", "wind_speed_10m","wind_direction_10m"]
    }

    try:
        # Make the request
        response = requests.get(OPEN_METEO_URL, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the JSON response
        data = response.json()

        # Extract relevant data
        return data.get("current", {})

    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

def fetch_hourly_forcast(lat, lon, days):
    # API parameters
    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": "temperature_2m,relative_humidity_2m,rain,wind_speed_10m,wind_direction_10m",
        "current_weather": True,  # Include the current weather
        "forecast_days": days
        #"timezone": "Asia%2FJerusalem",
    }

    try:
        # Make the request
        response = requests.get(OPEN_METEO_URL, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the JSON response
        data = response.json()

        # Extract relevant data
        return data.get("hourly", {})

    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

def fetch_daily_forcast(lat,lon,days):
    # API parameters
    params = {
        "latitude": lat,
        "longitude": lon,
        "daily": ["weather_code", "temperature_2m_max", "temperature_2m_min", "sunrise", "sunset"]
        #"timezone":
    }

    try:
        # Make the request
        response = requests.get(OPEN_METEO_URL, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the JSON response
        data = response.json()

        # Extract relevant data
        return data.get("daily", {})

    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


def get_weather_forecast(lat, lon):
    # Open-Meteo API URL
    url = "https://api.open-meteo.com/v1/forecast"

    # API parameters
    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": "temperature_2m,relative_humidity_2m,rain,wind_speed_10m,wind_direction_10m,weathercode",
        "current_weather": True,  # Include the current weather
        "daily": "weather_code,sunrise,sunset,uv_index_max",
        #"timezone": "Asia%2FJerusalem",
    }

    try:
        # Make the request
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the JSON response
        data = response.json()

        # Extract relevant data
        current_weather = data.get("current_weather", {})
        hourly_forecast = data.get("hourly", {})

        if current_weather:
            temperature = current_weather.get("temperature")
            humidity = hourly_forecast.get("relative_humidity_2m", [None])[0]
            rain = hourly_forecast.get("rain", [None])[0]
            wind_speed = current_weather.get("windspeed")
            wind_direction = current_weather.get("winddirection")
            weather_code = hourly_forecast.get("weathercode", [None])[0]

            return {
                "Temperature": temperature,
                "Humidity": humidity,
                "Rain prob.": rain,
                "Wind Speed": wind_speed,
                "Wind direction": wind_direction,
                "Weather code": weather_code,
            }
        else:
            return {"error": "No current weather data available"}

    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


# Example usage:
latitude = 40.7128  # Replace with your latitude
longitude = -74.0060  # Replace with your longitude
weather_data = get_weather_forecast(latitude, longitude)
#print(weather_data)
