import pandas as pd

from weather_forecast.forecast_presenter import *
import streamlit as st

def current_weather_widget(country_name,city_name,lat,lon):
    st.markdown("____")
    current_weather = current_weather_presenter(lat,lon)
    name, temperature, code = st.columns(3)
    humidity, wind_speed, wind_direction = st.columns(3)

    name.metric(country_name,city_name)
    temperature.metric("Temperature",str(current_weather["temperature"])+" °C","Feels like: "+str(current_weather["apparent_temperature"])+ " °C",delta_color="off",border=False)
    code.metric("Description", parse_weather_code_util(current_weather["weather_code"]),border=False)
    humidity.metric("Humidity",str(current_weather["humidity"])+"%",border=True)
    wind_speed.metric("Wind Speed",str(current_weather["wind_speed"])+" Km/h",border=True)
    wind_direction.metric("Wind Direction", parse_wind_direction_util(current_weather["wind_direction"]),border=True)

def hourly_data_widget(lat,lon,days=7):
    st.markdown("____")
    st.subheader("Next week forecast")
    st.text("(Zoom in to show hours)")

    dataframe = hourly_data_presenter(lat,lon,days)

    show_temperature, show_humidity, show_rain = st.columns(3)
    temperature_checked = show_temperature.checkbox("Temperature", value=True)
    humidity_checked = show_humidity.checkbox("Humidity", value=True)
    rain_checked = show_rain.checkbox("Rain probability", value=True)

    if temperature_checked:
        st.line_chart(dataframe, x="datetime", y="temperature")

    if humidity_checked:
        st.line_chart(dataframe, x="datetime", y="humidity")

    if rain_checked:
        st.bar_chart(dataframe, x="datetime", y="rain probability")

def hourly_wind_data_widget(lat,lon,days=7):
    st.markdown("____")
    st.subheader("Wind Forecast")
    st.text("(Zoom in to show hours)")
    is_hide = st.checkbox("hide",value=False)
    if  not is_hide:
        dataframe = hourly_wind_data_presenter(lat,lon,days)
        st.scatter_chart(dataframe,
                         x="datetime", x_label="Date",
                         y="wind_speed", y_label="Speed [Km/h]",
                         color="wind_direction")

def daily_data_widget(lat,lon,days=7):
    st.markdown("____")
    st.subheader("Additional Information")
    dataframe = daily_data_presenter(lat,lon,days)
    st.table(dataframe)

hourly_data_widget(32.0871000,34.8875000)