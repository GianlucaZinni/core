import os
from os import getenv


class Config:
    # Each Flask web application contains a secret key which used to sign session cookies for protection against cookie data tampering.
    SECRET_KEY = getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = getenv("DATABASE_URI")

    # Grabs the folder where the script runs.
    basedir = os.path.abspath(os.path.dirname(__file__))
    
    asgi = "3.0"
    
    # Enable debug mode, that will refresh the page when you make changes.
    DEBUG = True

    # Turn off the Flask-SQLAlchemy event system and warning
    SQLALCHEMY_TRACK_MODIFICATIONS = False