from city_geolocation import city_factory

def handle_city_name(city_name):
    if city_name != '':
        return city_factory.new_city_by_name(city_name)

def handle_city_location(lat,lon):
    return city_factory.new_city_by_location(lat,lon)