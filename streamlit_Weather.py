import streamlit as st
#import requests
#import psycopg2
import pandas as pd

st.title('Welcome to our Weather App')

# Initialize connection.
conn = st.connection("pagila", type="sql")

# Perform query.
df = conn.query('SELECT * FROM weather limit 15')

# Print results.
for row in df.itertuples():
    st.write(f"{row.location}")


