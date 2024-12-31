from city_geolocation.city_widget import *
from weather_forecast.forecast_widget import *

if __name__ == "__main__":

    st.title("Hakol BesWeather!")
    city = city_choose_method()

    if(city is not None):
        hourly_data_widget(city.latitude,city.longitude)

