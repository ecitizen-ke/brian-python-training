from flask import Flask
import os


def create_app():
    '''this function returns a Flask object'''
    app = Flask(__name__)
    # app.config['DEBUG'] = True
    # app.config['TESTING'] = True
    # print(app.config)
    return app
