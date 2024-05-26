from flask import Flask
from home_page_app import home_bp


app = Flask(__name__)
app.register_blueprint(home_bp)

if __name__ == '__main__':
    app.run(debug=True)
