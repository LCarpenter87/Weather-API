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
        return weather
    except:
        return 'Error', np.NAN, np.NAN, np.NAN
    
# List of cities
cities = ['London', 'Manchester', 'Birmingham', 'Glasgow', 'Leeds', 'Liverpool', 'Sheffield', 'Bristol', 'Edinburgh', 'Leicester',  'York', 'Cardiff', 'Brighton', 'Coventry', 'Bath']
selected_city = st.sidebar.selectbox('Select a city', cities)

weather_data = get_details(selected_city)

if weather_data:
    st.title(f"Weather Information for {selected_city}")
    st.write(f"Temperature: {weather_data['current']['temp_c']}°C")
    st.write(f"Condition: {weather_data['current']['condition']['text']}")
    st.write(f"Humidity: {weather_data['current']['humidity']}%")
    st.write(f"Wind Speed: {weather_data['current']['wind_kph']} km/h")
    st.write(f"Cloud Cover: {weather_data['current']['cloud']}%")
    st.write(f"UV Index: {weather_data['current']['uv']}")
else:
    st.error("Failed to fetch weather data. Please try again later.")


# Initialize connection.
#conn = st.connection("pagila", type="sql")

# Perform query.
#df = conn.query('SELECT * FROM weather limit 15')
#st.write(df)


