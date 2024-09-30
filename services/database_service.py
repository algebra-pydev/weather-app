"""
Owner: Algebra University, Zagreb
Address: Gradišćanska 24, 10000 Zagreb, Croatia
Web: www.algebra.hr
VAT-ID: 10750578045

Last modified: 2024-09-29

NOTE: This script is the property of Algebra University, Zagreb. Unauthorized use is strictly prohibited.
"""

from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship, joinedload
from models.city import City
from models.weather import Weather

Base = declarative_base()


class CityRecord(Base):
    """
    Represents a city in the database.

    Attributes:
        id (int): The unique identifier of the city.
        name (str): The name of the city.
        country (str): The country where the city is located.
    """
    __tablename__ = 'city_records'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    country = Column(String, nullable=False)

    weather_records = relationship("WeatherRecord", back_populates="city")

    def __init__(self, city: City):
        """
        Initializes the CityRecord object with data from a City instance.

        Args:
            city (City): The City object containing the city's data.
        """
        self.name = city.name
        self.country = city.country


class WeatherRecord(Base):
    """
    Represents a record of weather data in the database.

    Attributes:
        id (int): The unique identifier of the record.
        temperature (float): The recorded temperature.
        humidity (int): The recorded humidity (percentage).
        pressure (int): The recorded atmospheric pressure (hPa).
        condition (str): The weather condition (e.g., 'Clear', 'Clouds').
        wind_speed (float): The recorded wind speed (m/s).
        city_id (int): Foreign key that links the weather record to a city.
    """
    __tablename__ = 'weather_records'

    id = Column(Integer, primary_key=True)
    temperature = Column(Float, nullable=False)
    humidity = Column(Integer, nullable=False)
    pressure = Column(Integer, nullable=False)
    condition = Column(String, nullable=False)
    wind_speed = Column(Float, nullable=False)
    city_id = Column(Integer, ForeignKey('city_records.id'), nullable=False)
    city_name = Column(String, ForeignKey('cities.name'))
    city_country = Column(String, ForeignKey('cities.country'))

    city = relationship("CityRecord", back_populates="weather_records")

    def __init__(self, weather: Weather, city_record: CityRecord):
        """
        Initializes the WeatherRecord object with data from a Weather instance and its associated CityRecord.

        Args:
            weather (Weather): The Weather object containing weather data.
            city_record (CityRecord): The CityRecord object representing the city associated with the weather data.
        """
        self.temperature = weather.temperature
        self.humidity = weather.humidity
        self.pressure = weather.pressure
        self.condition = weather.condition
        self.wind_speed = weather.wind_speed
        self.city = city_record


class DatabaseService:
    """
    A service for interacting with the SQLite database using SQLAlchemy.

    Attributes:
        db_url (str): The URL of the SQLite database.
        engine (Engine): The SQLAlchemy engine for the database.
        Session (sessionmaker): The SQLAlchemy sessionmaker for creating sessions.
    """

    def __init__(self, db_url="sqlite:///data/weather.db"):
        """
        Initializes the DatabaseService with a connection to the SQLite database.

        Args:
            db_url (str): The URL for connecting to the SQLite database (default is 'sqlite:///data/weather.db').
        """
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)
        Base.metadata.create_all(self.engine)

    def add_city(self, city: City) -> CityRecord:
        """
        Adds a city to the database if it doesn't already exist, and returns the CityRecord.

        Args:
            city (City): The City object containing city data.

        Returns:
            CityRecord: The CityRecord object representing the city.
        """
        session = self.Session()
        try:
            # Check if city already exists
            city_record = session.query(CityRecord).filter_by(name=city.name, country=city.country).first()
            if not city_record:
                city_record = CityRecord(city)
                session.add(city_record)
                session.commit()
            return city_record
        except Exception as e:
            session.rollback()
            print(f"Error adding city record: {e}")
        finally:
            session.close()

    def add_weather_record(self, weather: Weather):
        """
        Adds a weather record to the database, linked to the corresponding city.

        Args:
            weather (Weather): The Weather object containing the weather data to store.
        """
        session = self.Session()
        try:
            # Add or get the city record
            city_record = self.add_city(weather.city)

            # Create and add the weather record linked to the city
            weather_record = WeatherRecord(weather, city_record)
            session.add(weather_record)
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"Error adding weather record: {e}")
        finally:
            session.close()

    def get_weather_records_for_city(self, city: City):
        """
        Retrieves all weather records for a specific city from the database.

        Args:
            city (City): The City object representing the city to retrieve weather data for.

        Returns:
            List[WeatherRecord]: A list of WeatherRecord objects for the specified city.
        """
        # session = self.Session()
        try:
            with self.Session() as session:
                return (
                    session.query(WeatherRecord)
                    .filter(
                            WeatherRecord.city_name == city.name,
                            WeatherRecord.city_country == city.country
                    )
                    .options(joinedload(WeatherRecord.city))
                    .all()
                )
        except Exception as e:
            print(f"Error retrieving weather records: {e}")
            return []
        # finally:
        #     session.close()
