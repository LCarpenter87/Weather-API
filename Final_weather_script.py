import psycopg2
import requests
import pandas as pd
from datetime import datetime

# Function to get weather details for a given city
def get_weather_details(cities):
    try:
        url = f'http://api.weatherapi.com/v1/current.json?key=787a74aa607147a19bb222554241903&q={cities}&aqi=yes'
        response = requests.get(url)
        weather_data = response.json()
        
        location = weather_data['location']
        current = weather_data['current']

        data = {
            'location': location['name'],
            'country': location['country'],
            'date': datetime.strptime(current['last_updated'], '%Y-%m-%d %H:%M').date(),
            'current_time': datetime.strptime(location['localtime'], '%Y-%m-%d %H:%M'),
            'time_updated': datetime.strptime(current['last_updated'], '%Y-%m-%d %H:%M'),
            'temperature': current['temp_c'],
            'condition_text': current['condition']['text'],
            'wind_speed_mph': current['wind_mph'],
            'wind_direction': current['wind_dir'],
            'humidity': current['humidity'],
            'cloud': current['cloud'],
            'uv_index': current['uv'],
            'co': current['air_quality']['co'],
            'no2': current['air_quality']['no2'],
            'o3': current['air_quality']['o3']}
     
        return data
    except Exception as e:
        print(f"Error: {e}")
        return None


# Include city names in a list:
city_names = ['London', 'Manchester', 'Birmingham', 'Glasgow', 'Leeds', 'Liverpool', 'Sheffield', 'Bristol', 'Edinburgh', 'Leicester',  'York', 'Cardiff', 'Brighton', 'Coventry', 'Bath']

# Create a dictionary to store weather data for each city
weather_data = {}

# weather data for each city:
for cities in city_names:
    data = get_weather_details(cities)
    if data:
        weather_data[cities] = data

# Function to load config from file
def load_config(filename):
    config = {}
    with open(filename, 'r') as file:
        for line in file:
            key, value = line.strip().split('=')
            config[key] = value
    return config



# Connect to database, creating table in DBeaver pagilla and inserting data onto there.
def connect_to_database(config, weather_data):
    conn = None
    cur = None
    try:
        conn = psycopg2.connect(
            dbname=config['dbname'],
            user=config['user'],
            password=config['password'],
            host=config['host'],
            port="5432")
        cur = conn.cursor()
        create_script = ''' CREATE TABLE IF NOT EXISTS student.weather (
                            location varchar(20),
                            country varchar(40),
                            date DATE,
                            "current_time" TIME,
                            time_updated TIME,
                            temperature INT,  
                            condition TEXT,
                            wind_speed_mph INT,
                            wind_direction TEXT,
                            humidity INT,
                            cloud INT,
                            uv_index INT,
                            co INT,
                            no2 INT,
                            o3 INT) '''
        if create_script:
            cur.execute(create_script)
            conn.commit()  # commit and save any transactions done into the DB.        
        
        # Loop weather data for each city and insert into the DB for updates:
        for city, data in weather_data.items():
            insert_query = ''' INSERT INTO student.weather (
                                    location, country, date, "current_time", time_updated, temperature,
                                    condition, wind_speed_mph, wind_direction, humidity,
                                    cloud, uv_index, co, no2, o3)
                               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) '''
            data_values = tuple(data.values())
            cur.execute(insert_query, data_values)
            conn.commit()  # Commit the transaction

        print("Data uploaded successfully! Yay!!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close() #close connnection

# main function to wrap everything together, use secrets txt called config to acccess database details, then connect to database:
def main():
    if weather_data:
        config = load_config('akshaya_secrets.txt')

        # Connect to database and insert data
        connect_to_database(config, weather_data)
    else:
        print("No weather data available.")

main()