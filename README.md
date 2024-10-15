# Weather-Fetcher-Using-API
Using python building a Weather Fetcher Using API

1. Set Up the Project
You'll need an API key from a weather service provider (such as OpenWeatherMap, WeatherAPI, etc.). For this example, I'll use OpenWeatherMap. Create an account at OpenWeatherMap and get your API key.

2. Install Required Libraries
Ensure you have requests installed in your environment. You can install it using:

bash
Copy code
pip install requests
3. Python Code for Weather Fetcher
Here's a basic script to fetch weather data using the OpenWeatherMap API:

python
Copy code
import requests
import json

# Replace with your OpenWeatherMap API key
API_KEY = 'your_openweathermap_api_key'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    try:
        # Constructing the final API call URL
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        # Check if the request was successful
        if data['cod'] != 200:
            print(f"City not found: {data['message']}")
            return None

        # Extract relevant weather information
        weather_info = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'description': data['weather'][0]['description'],
            'wind_speed': data['wind']['speed'],
        }

        return weather_info

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return None

def display_weather(city):
    weather_data = get_weather(city)
    if weather_data:
        print(f"Weather in {weather_data['city']}:")
        print(f"Temperature: {weather_data['temperature']}°C")
        print(f"Humidity: {weather_data['humidity']}%")
        print(f"Condition: {weather_data['description']}")
        print(f"Wind Speed: {weather_data['wind_speed']} m/s")
    else:
        print("Unable to fetch weather data.")

if __name__ == "__main__":
    city_name = input("Enter city name: ")
    display_weather(city_name)
4. How it Works
This script uses the OpenWeatherMap API to get weather data for a given city.
The user is prompted to input a city name, and the API call is made.
The response is processed, and relevant data like temperature, humidity, weather condition, and wind speed is printed.
5. Environment Variables for Security
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

python
Copy code
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'
