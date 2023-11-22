from datetime import datetime

import pytz
import requests


def get_weather_data(city, api_key):
    # URL to fetch weather data from OpenWeatherMap
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    # Making a request to the API
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather_data = [# OpenWeatherMap does not provide direct precipitation data
            f"temp {data['main']['temp']}°C",
            f"wind_sp {data['wind']['speed']} km/h",
            f'wind_dir {data["wind"]["deg"]}',
        ]
        return weather_data
    else:
        return "Error fetching data"


"""# Example usage
api_key = 'YOUR_API_KEY'  # Replace with your actual API key
city = 'London'
print(get_weather_data(city, api_key))"""


def get_moon_phase():
    # This function should calculate the current moon phase
    # Returning a mock value for illustration
    return "Full Moon"


def get_current_info():
    # Get current date and time
    now = datetime.now(pytz.timezone("UTC"))  # Replace 'UTC' with your desired timezone
    date = now.strftime("%Y-%m-%d")
    time_12hr = now.strftime("%I:%M %p")

    # Get weather data
    weather_data = get_weather_data()

    # Get moon phase
    moon_phase = get_moon_phase()

    return {
        "date": date,
        "time_12hr": time_12hr,
        "moon_phase": moon_phase,
        "precip": weather_data["precip"],
        "temp": weather_data["temp"],
        "wind_sp": weather_data["wind_sp"],
        "wind_dir": weather_data["wind_dir"],
    }
