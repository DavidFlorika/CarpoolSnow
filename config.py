import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'yoursecretkey'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///carpoolsnow.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False