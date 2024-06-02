from flask import Flask
import os


def create_app():
    app = Flask(__name__)
    if os.getenv("ENV")=="development":
        app.config.from_object("config.DevelopmentConfig")
    elif os.getenv("ENV")=="testing":
        app.config.from_object("config.TestingConfig")
    else:
        app.config.from_object("config.ProductionConfig")
    return app
