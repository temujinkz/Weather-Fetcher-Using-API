import requests
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()

API_KEY = os.getenv('API_KEY')
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    try:
        # Construct the full API URL with city and API key
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        # Check if the response is valid
        if data['cod'] != 200:
            print(f"City not found: {data['message']}")
            return None

        # Extract weather details
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
