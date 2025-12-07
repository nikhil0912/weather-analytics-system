"""
Configuration settings for Weather Analytics System
"""
import os
from dotenv import load_dotenv

load_dotenv()

# Flask Configuration
DEBUG = os.getenv('DEBUG', False)
TESTING = os.getenv('TESTING', False)
SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
JSONIFY_PRETTYPRINT_REGULAR = True

# API Keys
OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY', '')
WEATHER_GOV_API_KEY = os.getenv('WEATHER_GOV_API_KEY', '')

# Database Configuration
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///weather_data.db')
SQLALCHEMY_DATABASE_URI = DATABASE_URL
SQLALCHEMY_TRACK_MODIFICATIONS = False

# API Configuration
API_TIMEOUT = 30  # seconds
API_RETRY_ATTEMPTS = 3
API_RETRY_DELAY = 2  # seconds

# Data Configuration
DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
MODEL_DIR = os.path.join(os.path.dirname(__file__), 'models')

# Model Configuration
MODEL_PATH = os.path.join(MODEL_DIR, 'weather_model.pkl')
SCALER_PATH = os.path.join(MODEL_DIR, 'scaler.pkl')

# Logging Configuration
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

# Feature Configuration
FEATURES_TO_USE = [
    'temperature',
    'humidity',
    'pressure',
    'wind_speed',
    'precipitation',
    'cloud_coverage'
]

# Target Configuration
TARGET_VARIABLE = 'temperature'

# Model Hyperparameters
MODEL_PARAMS = {
    'n_estimators': 100,
    'max_depth': 10,
    'min_samples_split': 5,
    'min_samples_leaf': 2,
    'random_state': 42
}

# Forecast Configuration
FORECAST_DAYS = 7
FORECAST_HORIZON = 24  # hours

# Location Configuration
DEFAULT_LOCATION = 'New York'
DEFAULT_LATITUDE = 40.7128
DEFAULT_LONGITUDE = -74.0060

# Cache Configuration
CACHE_TIMEOUT = 3600  # seconds (1 hour)
CACHE_TYPE = 'simple'
