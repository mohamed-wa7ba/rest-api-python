import os
from dotenv import load_dotenv
load_dotenv() 
class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', '5f8b5a7e3c8d0b1e5f8b5a7e3c8d0b1e5f8b5a7e3c8d0b1e5f8b5a7e3c8d0b1e')
    DEBUG = os.getenv('DEBUG', 'False') == 'True'

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}