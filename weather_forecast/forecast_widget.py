from weather_forecast.forecast_presenter import *
import streamlit as st

def hourly_data_widget(lat,lon,days=7):
    dataframe = hourly_data_presenter(lat,lon,days)
    #st.table(dataframe)
    st.line_chart(dataframe, x="datetime", y="temperature")
    st.line_chart(dataframe, x="datetime", y="humidity")
    st.bar_chart(dataframe, x="datetime", y="rain probability")
