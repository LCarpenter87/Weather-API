import streamlit as st
import psycopg2
import pandas as pd

def load_config(filename):
    config = {}
    with open(filename, 'r') as file:
        for line in file:
            key, value = line.strip().split('=')
            config[key] = value
    return config

def connect_to_database():
    try:
        conn = psycopg2.connect(
            dbname=config['dbname'],
            user=config['user'],
            password=config['password'],
            host=config['host'],
            port="5432")
        cur = conn.cursor()
        print("connection uccessful!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close() #close connnection

conn = connect_to_database()


def main():
    if weather_data:
        config = load_config('akshaya_secrets.txt')

        # Connect to database and insert data
        connect_to_database(config, weather_data)
    else:
        print("No weather data available.")

main()