"""
Weather Data Fetcher Module
Handles fetching weather data from multiple API sources
"""
import requests
import logging
from typing import Dict, Optional, List
from datetime import datetime, timedelta
import config

logger = logging.getLogger(__name__)

class WeatherFetcher:
    """Fetches weather data from OpenWeatherMap and other sources"""
    
    def __init__(self, api_key: str = None):
        """Initialize weather fetcher with API key"""
        self.api_key = api_key or config.OPENWEATHER_API_KEY
        self.base_url = "https://api.openweathermap.org/data/2.5"
        self.timeout = config.API_TIMEOUT
        self.retry_attempts = config.API_RETRY_ATTEMPTS
        
    def get_current_weather(self, city: str, **kwargs) -> Dict:
        """Fetch current weather for a city"""
        try:
            params = {
                'q': city,
                'appid': self.api_key,
                'units': 'metric'
            }
            params.update(kwargs)
            
            response = requests.get(
                f"{self.base_url}/weather",
                params=params,
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logger.error(f"Error fetching weather: {e}")
            raise
    
    def get_forecast(self, city: str, days: int = 5, **kwargs) -> Dict:
        """Fetch weather forecast"""
        try:
            params = {
                'q': city,
                'appid': self.api_key,
                'units': 'metric',
                'cnt': days * 8
            }
            params.update(kwargs)
            
            response = requests.get(
                f"{self.base_url}/forecast",
                params=params,
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logger.error(f"Error fetching forecast: {e}")
            raise
    
    def get_coordinates(self, city: str) -> tuple:
        """Get latitude and longitude for a city"""
        weather_data = self.get_current_weather(city)
        coords = weather_data['coord']
        return coords['lat'], coords['lon']
    
    def validate_data(self, data: Dict) -> bool:
        """Validate fetched weather data"""
        required_fields = ['main', 'weather', 'wind']
        return all(field in data for field in required_fields)
