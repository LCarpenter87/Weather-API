import streamlit as st
import psycopg2
import pandas as pd

@st.cache_resource
def init_connection():
    return psycopg2.connect(**st.secrets["pagilla"])

conn = init_connection()

@st.cache_data(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

rows = run_query("SELECT * from weather limit 20")

data=pd.DataFrame(rows)
data.columns=['location', 'date', 'current_time', 'time_updated', 'temperature', 'condition', 'wind_speed_mph', 'wind_direction', 'humidity', 'cloud', 'uv_index', 'co', 'no2', 'o3']
st.table(data)
