import os

class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///banks.db"
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = "Miriam&&mikeyarethebestduo"

    DEBUG = True