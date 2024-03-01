import os

from dotenv import load_dotenv

# Load the stored environment variables
load_dotenv()

# Get the values
api_key = os.getenv("API_KEY")
database_url = os.getenv("DATABASE_URL")
secret = os.getenv("SECRET_KEY")

# Print the values
print(f"API_KEY = {api_key}")
print(f"DATABASE_URL = {database_url}")
print(f"SECRET = {secret}")
