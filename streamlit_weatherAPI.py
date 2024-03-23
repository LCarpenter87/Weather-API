import streamlit as st
import psycopg2
import pandas as pd


# Initialize connection.
conn = st.connection("pagilla_db", type="sql")

# Perform query.
df = conn.query('SELECT * FROM weather;', ttl="10m")
