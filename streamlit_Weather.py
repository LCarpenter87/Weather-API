import streamlit as st
import requests
import psycopg2
import pandas as pd

st.title('Welcome to our Weather App')

# Initialize database connection

@st.cache
def init_connection():
    conn = psycopg2.connect(
        db_name=st.secrets['DB_NAME']
        db_user=st.secrets['DB_USER']
        db_password=st.secrets['DB_PASSWORD']
        db_host=st.secrets['DB_HOST']
        DB_PORT=5432
    )
    return conn

# Use the connection
conn = init_connection()


