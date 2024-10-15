# Steps:
Install Required Libraries:

Install requests and python-dotenv if not installed:

pip install requests python-dotenv
Create a .env File:

In the same directory as main.py, create a file named .env:
makefile
Copy code
API_KEY=your_openweathermap_api_key
Run the Script:

Run the script, enter a city name, and see the current weather details.
bash
Copy code
python main.py
This single main.py file handles fetching and displaying weather data using the API key securely stored in a .env file.
