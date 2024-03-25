import os 
from sqlalchemy import create_engine

""" Modify the class Config if you need to change the configurations for your local environment."""

class Config(object):
    SECRET_KEY='SECRET'
    SESSION_COOKIE_SECURE=False

class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:Logd031211@localhost:3306/sir_cookie'

