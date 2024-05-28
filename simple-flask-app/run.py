from flask import Flask, jsonify
from bp_app.index import index_bp
from bp_app.products import products_bp
from bp_app.users import users_bp

app = Flask(__name__)
app.register_blueprint(index_bp)
app.register_blueprint(products_bp)
app.register_blueprint(users_bp)

if __name__ == '__main__':
    app.run(debug=True)
