import streamlit as st
import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

st.title('Welcome to the Weather App')

def connect():
    try:
        conn = psycopg2.connect(
            dbname=st.secrets['dbname'],
            user=st.secrets['user'],
            password=st.secrets['password'],
            host=st.secrets['host'],
            port="5432")
        st.write("Connected to the database!")
        cur = conn.cursor()
        cur.execute("SELECT * FROM student.weather limit 10")
        rows = cur.fetchall()
        for row in rows:
            st.write(row)

    except Exception as e:
        st.error(f"Unable to connect to the database: {e}")
    finally:
        if conn is not None:
            conn.close()
