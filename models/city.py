"""
Owner: Algebra University, Zagreb
Address: Gradišćanska 24, 10000 Zagreb, Croatia
Web: www.algebra.hr
VAT-ID: 10750578045

Last modified: 2024-09-29

NOTE: This script is the property of Algebra University, Zagreb. Unauthorized use is strictly prohibited.
"""

class City:
    """
    Represents a city for which weather data can be retrieved.

    Attributes:
        name (str): The name of the city.
        country (str): The country where the city is located.
    """

    def __init__(self, name: str, country: str):
        """
        Initializes the City object with a name and country.

        Args:
            name (str): The name of the city.
            country (str): The country where the city is located.
        """
        self.name = name
        self.country = country

    def get_full_name(self) -> str:
        """
        Returns the full name of the city in the format 'City, Country'.

        Returns:
            str: The full name of the city including its country.
        """
        return f"{self.name}, {self.country}"

    def __repr__(self) -> str:
        """
        Returns a string representation of the City object for debugging purposes.

        Returns:
            str: A string representation of the City object.
        """
        return f"City(name='{self.name}', country='{self.country}')"
