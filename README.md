# Weather app
**Module 03 - Projektna aplikacija**

## Konzolna aplikacija za vremensku prognozu

Ova aplikacija omogućuje korisnicima dohvaćanje vremenske prognoze za odabrane gradove i pohranjuje povijest prognoza u lokalnu SQLite bazu podataka.

## Instalacija

1. Klonirajte repozitorij ili preuzmite kod.
2. Instalirajte potrebne pakete pomocu requirements.txt datoteke (`pip install -r requirements.txt`)
3. U datoteci .env umjesto `your_openweathermap_api_key_here` upisite Vas OpenWeatherMap API key 


## Korištenje

Slijedite upute prikazane u konzoli za odabir opcija kao što su:

- Dodavanje novog grada
- Prikaz trenutne vremenske prognoze
- Pregled povijesti prognoza


## Struktura aplikacije

weather_app/   
├── main.py  
├── models/  
│   ├── __init__.py  
│   ├── city.py  
│   └── weather.py  
├── services/  
│   ├── __init__.py  
│   ├── api_service.py (requests i json)  
│   └── database_service.py (SQLite i SQL Alchemy)  
├── utils/  
│   ├── __init__.py  
│   ├── formatters.py (prikaz teksta)  
│   └── helpers.py  
├── data/  
│   └── weather.db  
├── requirements.txt  
└── README.md



