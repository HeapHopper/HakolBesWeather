class City:
    def __init__(self, city: str, country: str, latitude: float, longitude: float):
        self.city = city
        self.country = country
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return f"Location(city='{self.city}', country='{self.country}', latitude={self.latitude}, longitude={self.longitude})"

    def params(self):
        return self.city, self.country, self.latitude, self.longitude

