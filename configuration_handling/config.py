
class Config(object):
    
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'TGTGFHGFV'
    DB_NAME = 'production_db'
    DB_USERNAE = 'root'
    DB_PASSWORD = 'password'
    UPLOADS = ''
    SESSION_COOKIE_SECURE = True
    
class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True    
    
    DB_NAME = 'development_db'
    DB_USERNAE = 'root'
    DB_PASSWORD = 'password'
    SESSION_COOKIE_SECURE = False
    
class TestingConfig(Config):
    TESTING = True  
     
    DB_NAME = 'testing_db'
    DB_USERNAE = 'root'
    DB_PASSWORD = 'password'
    SESSION_COOKIE_SECURE = False
    
     
        