import os
class Config(object):

    DEBUG =''
    TESTING = ''
    HOST = ''
    DB = ''
    USER = ''
    PASSWORD = ''

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = False
    HOST = os.getenv('HOST')
    DB = os.getenv('DB')
    DB_USER = os.getenv('DB_USER')
    PASSWORD = os.getenv('PASSWORD')

class TestingConfig(Config):
    TESTING = '' 
    HOST = ''
    DB = ''
    USER = ''
    PASSWORD = ''
    
    