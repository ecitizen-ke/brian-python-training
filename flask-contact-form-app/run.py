from flask import Flask
from home_page_app import home_bp
from contact_page_app import contact_bp


app = Flask(__name__)
app.secret_key = 'secret_key'
app.register_blueprint(home_bp)
app.register_blueprint(contact_bp)

if __name__ == '__main__':
    app.run(debug=True)
