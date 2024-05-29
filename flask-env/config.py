class config(object):
    DEBUG = False
    TEST = False
    SECRET_KEY = 'FDEWEDRFGFHGT'

    production_db = 'production_db'
    db_name = 'root'
    db_password = 'example'


class productionConfig(config):
    pass


class developmentConfig(config):
    DEBUG = True
    development_db = 'development_db'
    db_name = 'root'
    db_password = 'example1'


class testConfig(config):
    TEST = False
    test_db = 'test_db'
    db_name = 'root'
    db_password = 'example2'
