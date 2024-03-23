import streamlit as st
import psycopg2
import pandas as pd

conn = st.experimental_connection('pagilla_db', type='postgresql')
