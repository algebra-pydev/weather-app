"""
Owner: Algebra University, Zagreb
Address: Gradišćanska 24, 10000 Zagreb, Croatia
Web: www.algebra.hr
VAT-ID: 10750578045

Last modified: 2024-09-29

NOTE: This script is the property of Algebra University, Zagreb. Unauthorized use is strictly prohibited.
"""

from models.city import City
from models.weather import Weather
from services.database_service import WeatherRecord


def format_city(city: City) -> str:
    """
    Formats the City object for display.

    Args:
        city (City): The City object to be formatted.

    Returns:
        str: A formatted string representing the city (e.g., "Zagreb, HR").
    """
    return f"{city.name}, {city.country}"


def format_weather(weather: Weather) -> str:
    """
    Formats the Weather object for display.

    Args:
        weather (Weather): The Weather object to be formatted.

    Returns:
        str: A formatted string representing the weather data.
    """
    return (
        f"Weather in {weather.city.name}, {weather.city.country}:\n"
        f"  Temperature: {weather.temperature}°C\n"
        f"  Humidity: {weather.humidity}%\n"
        f"  Pressure: {weather.pressure} hPa\n"
        f"  Condition: {weather.condition}\n"
        f"  Wind Speed: {weather.wind_speed} m/s\n"
    )


def format_weather_record(record: WeatherRecord) -> str:
    """
    Formats a WeatherRecord object for display.

    Args:
        record (WeatherRecord): The WeatherRecord object to be formatted.

    Returns:
        str: A formatted string representing the weather record data.
    """
    return (
        f"Weather in {record.city_name}, {record.country}:\n"
        f"  Temperature: {record.temperature}°C\n"
        f"  Humidity: {record.humidity}%\n"
        f"  Pressure: {record.pressure} hPa\n"
        f"  Condition: {record.condition}\n"
        f"  Wind Speed: {record.wind_speed} m/s\n"
    )


def format_weather_history(records: list[WeatherRecord]) -> str:
    """
    Formats a list of WeatherRecord objects for display.

    Args:
        records (list[WeatherRecord]): A list of WeatherRecord objects to be formatted.

    Returns:
        str: A formatted string representing the list of weather records.
    """
    if not records:
        return "No weather history available."

    formatted_records = [format_weather_record(record) for record in records]
    return "\n".join(formatted_records)
