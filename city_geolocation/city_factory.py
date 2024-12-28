import requests
from city_geolocation.city import City

def new_city_by_location(latitude, longitude):
    city_name, country, latitude, longitude = __get_location_from_coordinates(latitude,longitude)
    return City(city_name,country,latitude,longitude)

def new_city_by_name(city_name):
    if city_name != '':
        city_name, country, latitude, longitude = __get_city_coordinates(city_name)
        return City(city_name,country,latitude,longitude)


def __get_city_coordinates(city_name):
    # Define the Nominatim API endpoint
    nominatim_url = "https://nominatim.openstreetmap.org/search"

    # Prepare the headers with a valid User-Agent (include your email if possible)
    headers = {
        'User-Agent': 'HakolBesWeather/1.0'  # Replace with your email or app name
    }

    # Send the request to the Nominatim API with parameters
    params = {
        'q': city_name,  # Query for the city name
        'format': 'json',  # Get response in JSON format
        'addressdetails': 1,  # Include detailed address information
        'limit': 1  # Limit to 1 result for simplicity
    }

    response = requests.get(nominatim_url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if data:
            city_data = data[0]
            lat = city_data['lat']
            lon = city_data['lon']
            country = city_data.get('address', {}).get('country', 'Unknown')

            return city_name, country, lat, lon
        else:
            print(f"No data found for city: {city_name}")
    else:
        print(f"Error fetching data: {response.status_code}")

def __get_location_from_coordinates(lat, lon):
    # Define the Nominatim reverse geocoding API endpoint
    nominatim_url = "https://nominatim.openstreetmap.org/reverse"

    # Prepare the headers with a valid User-Agent (replace with your email or app name)
    headers = {
        'User-Agent': 'MyGeoApp/1.0 (your-email@example.com)'  # Replace with your email
    }

    # Send the request to the Nominatim API for reverse geocoding
    params = {
        'lat': lat,  # Latitude of the location
        'lon': lon,  # Longitude of the location
        'format': 'json',  # Get response in JSON format
        'addressdetails': 1,  # Include detailed address information
    }

    response = requests.get(nominatim_url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if data:
            # Extract city and country from the response
            address = data.get('address', {})
            city = address.get('city', 'Unknown')
            country = address.get('country', 'Unknown')

            return city, country, lat, lon
        else:
            print("No data found for the given coordinates.")
            return None, None
    else:
        print(f"Error fetching data: {response.status_code}")
        return None, None