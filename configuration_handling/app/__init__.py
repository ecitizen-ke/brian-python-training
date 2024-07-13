from flask import Flask
import os


app = Flask(__name__)
if os.getenv("ENV")=="development":
    app.config.from_object("config.DevelopmentConfig")
elif os.getenv("ENV")=="testing":
    app.config.from_object("config.TestingConfig")
else:
    app.config.from_object("config.ProductionConfig")    
    

