import streamlit as st
import psycopg2
import pandas as pd

@st.cache_resource
def init_connection():
    return psycopg2.connect(**st.secrets["pagilla"])

conn = init_connection()

st.title('Welcome to our Weather App')

cur = conn.cursor()
cur.execute("SELECT * FROM student.weather limit 10")
data = cur.fetchall()

st.write(pd.DataFrame(data, columns=['Location', 'Country', 'Date', 'Current Time', 'Time Updated', 'Temperature', 'Condition', 'Wind Speed (mph)', 'Wind Direction', 'Humidity', 'Cloud', 'UV Index', 'CO', 'NO2', 'O3']))
conn.close()

