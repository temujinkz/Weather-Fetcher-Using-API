# 1. Set Up the Project
You'll need an API key from a weather service provider (such as OpenWeatherMap, WeatherAPI, etc.). For this example, I'll use OpenWeatherMap. Create an account at OpenWeatherMap and get your API key.

# 2. Install Required Libraries
Ensure you have requests installed in your environment. You can install it using: pip install requests

# 3. How it Works
This script uses the OpenWeatherMap API to get weather data for a given city.
The user is prompted to input a city name, and the API call is made.
The response is processed, and relevant data like temperature, humidity, weather condition, and wind speed is printed.

# 5. Environment Variables for Security
For security reasons, it's a good idea not to hardcode your API key. Use environment variables instead. Here’s how you can do that:

Install python-dotenv:

bash
Copy code
pip install python-dotenv
Create a .env file to store the API key:

makefile
Copy code
API_KEY=your_openweathermap_api_key
Modify the script to load the API key from .env:


import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

# Rest of the code remains the same
