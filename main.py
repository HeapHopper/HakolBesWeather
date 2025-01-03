import streamlit


from city_geolocation.city_widget import *
from map.map_widget import basic_map_widget
from weather_forecast.forecast_widget import *

if __name__ == "__main__":

    st.title("Hakol BesWeather!")
    st.image("assets/HakolBesWeather.png")

    city = city_choose_method()

    if(city is not None):
        current_weather_widget(city.country,city.city,city.latitude,city.longitude)
        basic_map_widget(city.latitude,city.longitude)
        hourly_data_widget(city.latitude,city.longitude)
        hourly_wind_data_widget(city.latitude,city.longitude)
        daily_data_widget(city.latitude,city.longitude)

