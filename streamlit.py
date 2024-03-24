import streamlit as st
import requests
import numpy as np
import sqlalchemy
#import psycopg2
import pandas as pd

st.title('Welcome to our Weather App')


def get_details(cities):
    try:
        url = f'http://api.weatherapi.com/v1/current.json?key=787a74aa607147a19bb222554241903&q={cities}&aqi=yes'
        response = requests.get(url)
        weather = response.json()
        temperature = weather['current']['temp_c']
        condition = weather['current']['condition']['text']
        icon = weather['current']['condition']['icon']
        humidity = weather['current']['humidity']
        Cloud_cover= weather['current']['cloud']
        UV_index= weather['current']['uv']
        CO = weather['current']['air_quality']['co']
        NO2= weather['current']['air_quality']['no2']
        Ozone= weather['current']['air_quality']['o3']
        return temperature, condition, icon, humidity, Cloud_cover, UV_index, CO, NO2, Ozone
        
    except:
        return 'Error', np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN

cities = ['London', 'Manchester', 'Birmingham', 'Glasgow', 'Leeds', 'Liverpool', 'Sheffield', 'Bristol', 'Edinburgh', 'Leicester',  'York', 'Cardiff', 'Brighton', 'Coventry', 'Bath']
selected_city = st.sidebar.selectbox('Select a city', cities)

weather_data = temperature, condition, icon, humidity, Cloud_cover, UV_index, CO, NO2, Ozone = get_details(selected_city)

if weather_data:
    st.title(f"{selected_city}")
    st.write(f"Temperature: {temperature}°C")
    st.write(f"Condition: {condition}")
    st.write(f"Humidity: {humidity}%")
    st.write(f"Cloud Cover: {Cloud_cover}%")
    st.write(f"UV Index: {UV_index}")
    st.write(f"CO: {CO}")
    st.write(f"NO2: {NO2}")
    st.write(F"Ozone (O3): {Ozone}")
    icon_url = "https:" + icon
    st.image(icon_url, caption='Weather Condition', use_column_width=True)

else:
    st.error("Failed to fetch weather data. Please try again later.")
