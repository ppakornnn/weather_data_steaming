import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variables
api_key = os.getenv("API_KEY")

# Set the API endpoint
url = "https://api.openaq.org/v3/countries/111"

# Define headers with the API key
headers = {
    "X-API-Key": api_key
}

# Make a GET request to the API
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    print("API response data:", data)
else:
    print("Request failed:", response.status_code, response.text)