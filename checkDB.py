from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get database credentials
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

# Print environment variables to check if they are loaded correctly
print("DB_NAME:", DB_NAME)
print("DB_USER:", DB_USER)
print("DB_PASSWORD:", DB_PASSWORD)
print("DB_HOST:", DB_HOST)
print("DB_PORT:", DB_PORT)