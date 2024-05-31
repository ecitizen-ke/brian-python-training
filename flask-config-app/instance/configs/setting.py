import os


class DefaultConfig(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY')


class DevelopmentConfig(DefaultConfig):
    SECRET_KEY = os.environ.get('SECRET_KEY')
