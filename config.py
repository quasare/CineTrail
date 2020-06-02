""" Flask Config """
from os import environ, path, getenv
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

class Config:
    """ Set Flask Config variable"""

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    SECRET_KEY = 'hTL0kdYHWbduXSAD7q4WgD4-N10vEFleQfO_xQx6-V0'
    SECURITY_PASSWORD_SALT = '156wg1ew651ewgwegwe'
    API_KEY = getenv('API_KEY')

class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'PROD_DATABASE_URI'


class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgres:///cinetrail'