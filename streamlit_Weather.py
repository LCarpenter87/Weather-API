import streamlit as st
import requests
import psycopg2
import pandas as pd

st.title('Welcome to our Weather App')
# Initialize database connection

# Set up database connection
dbname=st.secrets['db_name']
user=st.secrets['db_user']
password=st.secrets['db_password']
host=st.secrets['db_host']
port=5432

# Function to fetch weather details for a given city


