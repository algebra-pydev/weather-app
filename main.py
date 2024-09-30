"""
Owner: Algebra University, Zagreb
Address: Gradišćanska 24, 10000 Zagreb, Croatia
Web: www.algebra.hr
VAT-ID: 10750578045

Last modified: 2024-09-29

NOTE: This script is the property of Algebra University, Zagreb. Unauthorized use is strictly prohibited.
"""

import os
from dotenv import load_dotenv
from services.api_service import OpenWeatherMapService
from services.database_service import DatabaseService
from models.city import City
from utils.helpers import validate_city_name, validate_country_code
from utils.formatters import format_weather, format_weather_history

# Load environment variables from .env file
load_dotenv()

# Fetch the API key from the environment
api_key = os.getenv("OPENWEATHER_API_KEY")

# Check if the API key was loaded
if not api_key:
    raise Exception("API key not found. Please ensure OPENWEATHER_API_KEY is set in the .env file.")

# Initialize services
weather_service = OpenWeatherMapService(api_key)
db_service = DatabaseService()

def main_menu():
    """
    Displays the main menu for the weather application and handles user input.
    """
    while True:
        print("\nWeather App - Main Menu")
        print("1. Get weather data for a city")
        print("2. View weather history for a city")
        print("3. Add a new city to the database")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            get_weather_data()
        elif choice == '2':
            view_weather_history()
        elif choice == '3':
            add_city()
        elif choice == '4':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

def get_weather_data():
    """
    Gets weather data for a city from the API and stores it in the database.
    """
    city_name = input("Enter the name of the city: ").strip()
    if not validate_city_name(city_name):
        print("Invalid city name. Please use only letters and spaces.")
        return

    country_code = input("Enter the 2-letter country code (e.g., 'HR' for Croatia): ").strip().upper()
    if not validate_country_code(country_code):
        print("Invalid country code. Please provide a valid ISO 3166-1 alpha-2 country code.")
        return

    try:
        # Get weather data from the API
        weather = weather_service.get_weather_by_city_and_country(city_name, country_code)
        print(format_weather(weather))

        # Store the weather data in the database
        db_service.add_weather_record(weather)
        print("Weather data successfully saved to the database.")
    except Exception as e:
        print(f"Error retrieving weather data: {e}")

def view_weather_history():
    """
    Displays the weather history for a city from the database.
    """
    city_name = input("Enter the name of the city: ").strip()
    if not validate_city_name(city_name):
        print("Invalid city name. Please use only letters and spaces.")
        return

    country_code = input("Enter the 2-letter country code (e.g., 'HR' for Croatia): ").strip().upper()
    if not validate_country_code(country_code):
        print("Invalid country code. Please provide a valid ISO 3166-1 alpha-2 country code.")
        return

    city = City(city_name, country_code)
    records = db_service.get_weather_records_for_city(city)

    if records:
        print("\nWeather History:")
        print(format_weather_history(records))
    else:
        print("No weather history available for this city.")

def add_city():
    """
    Adds a new city to the database.
    """
    city_name = input("Enter the name of the city: ").strip()
    if not validate_city_name(city_name):
        print("Invalid city name. Please use only letters and spaces.")
        return

    country_code = input("Enter the 2-letter country code (e.g., 'HR' for Croatia): ").strip().upper()
    if not validate_country_code(country_code):
        print("Invalid country code. Please provide a valid ISO 3166-1 alpha-2 country code.")
        return

    city = City(city_name, country_code)
    try:
        db_service.add_city(city)
        print(f"City '{city_name}, {country_code}' successfully added to the database.")
    except Exception as e:
        print(f"Error adding city: {e}")

if __name__ == "__main__":
    main_menu()
