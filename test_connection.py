import os

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOSTS = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")



# Print all environment variables
for key, value in os.environ.items():
    print(f"{key}: {value}")