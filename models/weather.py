"""
Owner: Algebra University, Zagreb
Address: Gradišćanska 24, 10000 Zagreb, Croatia
Web: www.algebra.hr
VAT-ID: 10750578045

Last modified: 2024-09-29

NOTE: This script is the property of Algebra University, Zagreb. Unauthorized use is strictly prohibited.
"""

from models.city import City


class Weather:
    """
    Represents weather data for a specific city.

    Attributes:
        city (City): The City object representing the city for which the weather data is fetched.
        temperature (float): The current temperature in the city.
        humidity (int): The current humidity in the city (percentage).
        pressure (int): The current atmospheric pressure in hPa.
        condition (str): The general weather condition (e.g., 'Clear', 'Clouds').
        wind_speed (float): The wind speed in m/s.
    """

    def __init__(self, city: City, temperature: float, humidity: int, pressure: int, condition: str, wind_speed: float):
        """
        Initializes the Weather object with weather data for a specific city.

        Args:
            city (City): The City object representing the city.
            temperature (float): The current temperature in the city.
            humidity (int): The current humidity in the city (percentage).
            pressure (int): The current atmospheric pressure in hPa.
            condition (str): The general weather condition.
            wind_speed (float): The wind speed in m/s.
        """
        self.city = city
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.condition = condition
        self.wind_speed = wind_speed

    @classmethod
    def from_api_response(cls, response: dict):
        """
        Creates a Weather object from a JSON response provided by the OpenWeatherMap API.

        Args:
            response (dict): The JSON response from the OpenWeatherMap API containing weather data.

        Returns:
            Weather: A Weather object populated with the data from the API response.
        """
        city_name = response['name']
        country = response.get('sys', {}).get('country', 'Unknown')
        city = City(city_name, country)  # Use the City model to create a City instance

        temperature = response['main']['temp']
        humidity = response['main']['humidity']
        pressure = response['main']['pressure']
        condition = response['weather'][0]['main']
        wind_speed = response['wind']['speed']

        return cls(city, temperature, humidity, pressure, condition, wind_speed)

    def __repr__(self) -> str:
        """
        Returns a string representation of the Weather object for debugging purposes.

        Returns:
            str: A string representation of the Weather object.
        """
        return (f"Weather(city={self.city.get_full_name()}, temperature={self.temperature}, "
                f"humidity={self.humidity}, pressure={self.pressure}, "
                f"condition='{self.condition}', wind_speed={self.wind_speed})")
