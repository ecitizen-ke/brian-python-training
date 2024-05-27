from flask import Flask, jsonify
# from app.users import view_users
# from app.index import view_index
# from app.products import view_products
from bp_app.index import index_bp
app = Flask(__name__)
app.register_blueprint(index_bp)


# @app.route('/')
# def index():
#     return '<h1> hello, world! </h1>'


# @app.route('/users')
# def users():
#     dict = [{'username': 'admin', 'password': 'admin123'},
#             {'username': 'brian', 'password': 'brian123'}
#             ]
#     return jsonify(dict)


# @app.route('/products')
# def products():
#     dict = [{'fruits': ['apple', 'orange', 'banana']},
#             {'drinks': ['tea', 'cofee', 'orange']}]
#     return jsonify(dict)


# view_users(app)
# view_index(app)
# view_products(app)


if __name__ == '__main__':
    app.run(debug=True)
