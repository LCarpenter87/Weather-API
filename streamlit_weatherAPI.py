import streamlit as st
import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

@st.cache_resource
def init_connection():
    return psycopg2.connect(**st.secrets["pagilla"])

conn = init_connection()

st.title('Welcome to our Weather App')

@st.cache_data(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

rows = run_query("SELECT * from weather limit 20")

data=pd.DataFrame(rows)
#data.columns=['location', 'country', 'date', 'current_time', 'time_updated', 'temperature', 'condition', 'wind_speed_mph', 'wind_direction', 'humidity', 'cloud', 'uv_index', 'co', 'no2', 'o3']

st.write(data, columns=['Location', 'Date', 'Current Time', 'Time Updated', 'Temperature', 'Condition', 'Humidity', 'Cloud', 'UV Index', 'CO', 'NO2', 'O3'])
#st.table(data)
