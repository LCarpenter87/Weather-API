import os
import streamlit as st

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOSTS = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

print("DB_NAME:", DB_NAME)
print("DB_USER:", DB_USER)
print("DB_PASSWORD:", DB_PASSWORD)
print("DB_HOST:", DB_HOSTS)
print("DB_PORT:", DB_PORT)

DB_NAME = st.secrets["DB_NAME"]
DB_USER = st.secrets["DB_USER"]
DB_PASSWORD = st.secrets["DB_PASSWORD"]
DB_HOSTS = st.secrets["DB_HOSTS"]
DB_PORT = st.secrets["DB_PORT"]

print("DB_NAME:", DB_NAME)
print("DB_USER:", DB_USER)
print("DB_PASSWORD:", DB_PASSWORD)
print("DB_HOSTS:", DB_HOSTS)
print("DB_PORT:", DB_PORT)