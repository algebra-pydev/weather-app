"""
Owner: Algebra University, Zagreb
Address: Gradišćanska 24, 10000 Zagreb, Croatia
Web: www.algebra.hr
VAT-ID: 10750578045

Last modified: 2024-09-29

NOTE: This script is the property of Algebra University, Zagreb. Unauthorized use is strictly prohibited.
"""

import re

def validate_city_name(city_name: str) -> bool:
    """
    Validates the city name to ensure it only contains alphabetic characters and spaces.

    Args:
        city_name (str): The name of the city to validate.

    Returns:
        bool: True if the city name is valid, False otherwise.
    """
    if not city_name:
        return False
    return bool(re.match(r'^[a-zA-Z\s]+$', city_name))


def validate_country_code(country_code: str) -> bool:
    """
    Validates the country code to ensure it is a valid ISO 3166-1 alpha-2 country code (2 uppercase letters).

    Args:
        country_code (str): The country code to validate.

    Returns:
        bool: True if the country code is valid, False otherwise.
    """
    if len(country_code) != 2:
        return False
    return bool(re.match(r'^[A-Z]{2}$', country_code))


def kelvin_to_celsius(kelvin_temp: float) -> float:
    """
    Converts a temperature from Kelvin to Celsius.

    Args:
        kelvin_temp (float): The temperature in Kelvin.

    Returns:
        float: The temperature converted to Celsius.
    """
    return kelvin_temp - 273.15


def celsius_to_fahrenheit(celsius_temp: float) -> float:
    """
    Converts a temperature from Celsius to Fahrenheit.

    Args:
        celsius_temp (float): The temperature in Celsius.

    Returns:
        float: The temperature converted to Fahrenheit.
    """
    return (celsius_temp * 9/5) + 32


def validate_temperature_range(temperature: float) -> bool:
    """
    Validates that the temperature is within a realistic range for Earth (-100°C to 60°C).

    Args:
        temperature (float): The temperature to validate.

    Returns:
        bool: True if the temperature is within a valid range, False otherwise.
    """
    return -100 <= temperature <= 60
