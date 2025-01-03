import streamlit as st
import geocoder

from city_geolocation.city_controller import *

def city_choose_method():
    st.subheader("Pick your location!")
    # Radio button options
    options = ["Search city", "Get weather info by location coordinates (lat/lon)"]
    # Adding the radio button
    choice = st.radio("Pick a method to set the location for your weather update:", options)
    # Displaying the result based on user choice
    city = None
    if choice == "Search city":
        city = city_by_name_widget()
    elif choice == "Get weather info by location coordinates (lat/lon)":
        city = city_by_location_widget()

    return city


def city_by_name_widget():
    # Streamlit widget to input a city name
    st.write("Choosing location by name.")
    user_city_name = st.text_input("Enter a city name:", value=get_current_city())
    user_city = handle_city_name(user_city_name)
    #city_widget(user_city)
    return user_city

def city_by_location_widget():
    st.write("Choosing location by latitude/longitude.")
    user_city_lat = st.number_input("Enter a latitude:", format="%.7f", value=get_current_location()[0])
    user_city_lon = st.number_input("Enter a longitude:", format="%.7f", value=get_current_location()[1])
    user_city2 = handle_city_location(user_city_lat, user_city_lon)
    #city_widget(user_city2)
    return user_city2

def city_widget(city):
    if city is not None:
        city_name, country, latitude, longitude = city.params()
        # Aggregate the results into one widget
        output = f"""
        **City**: {city_name}  
        **Country**: {country}  
        **Latitude**: {latitude}  
        **Longitude**: {longitude}
        """
        st.markdown(output)  # Display the aggregated information

def get_current_city():
    g = geocoder.ip("me")
    device_city = g.geojson["features"][0]["properties"]["city"]
    return device_city

def get_current_location():
    g = geocoder.ip("me")
    device_lon, device_lat = g.geojson["features"][0]["geometry"]["coordinates"]
    return device_lat, device_lon