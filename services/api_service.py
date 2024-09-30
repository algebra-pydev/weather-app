"""
Owner: Algebra University, Zagreb
Address: Gradišćanska 24, 10000 Zagreb, Croatia
Web: www.algebra.hr
VAT-ID: 10750578045

Last modified: 2024-09-29

NOTE: This script is the property of Algebra University, Zagreb. Unauthorized use is strictly prohibited.
"""

import requests
from models.weather import Weather

class OpenWeatherMapService:
    """
    Service for interacting with the OpenWeatherMap API.

    Attributes:
        api_key (str): The API key used for authentication with the OpenWeatherMap API.
        base_url (str): The base URL for OpenWeatherMap API.
    """

    def __init__(self, api_key: str):
        """
        Initializes the OpenWeatherMapService with the provided API key.

        Args:
            api_key (str): The API key for OpenWeatherMap API.
        """
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def get_weather_by_city(self, city_name: str) -> Weather:
        """
        Fetches weather data for a specific city from OpenWeatherMap and returns a Weather object.

        Args:
            city_name (str): The name of the city to fetch weather data for.

        Returns:
            Weather: A Weather object containing the weather data for the specified city.

        Raises:
            Exception: If the API request fails or if the city is not found.
        """
        params = {
            "q": city_name,
            "appid": self.api_key,
            "units": "metric"  # To get the temperature in Celsius
        }

        response = requests.get(self.base_url, params=params)

        if response.status_code != 200:
            raise Exception(f"Error fetching weather data: {response.status_code}, {response.text}")

        data = response.json()
        return Weather.from_api_response(data)

    def get_weather_by_city_and_country(self, city_name: str, country_code: str) -> Weather:
        """
        Fetches weather data for a specific city and country from OpenWeatherMap and returns a Weather object.

        Args:
            city_name (str): The name of the city to fetch weather data for.
            country_code (str): The country code (ISO 3166) for the city.

        Returns:
            Weather: A Weather object containing the weather data for the specified city and country.

        Raises:
            Exception: If the API request fails or if the city is not found.
        """
        params = {
            "q": f"{city_name},{country_code}",
            "appid": self.api_key,
            "units": "metric"  # To get the temperature in Celsius
        }

        response = requests.get(self.base_url, params=params)

        if response.status_code != 200:
            raise Exception(f"Error fetching weather data: {response.status_code}, {response.text}")

        data = response.json()
        return Weather.from_api_response(data)
