from flask import jsonify
dict = [{'fruits': ['apple', 'orange', 'banana']},
        {'drinks': ['tea', 'cofee', 'orange']}]


def view_products(app):
    @app.route('/products')
    def product():
        return jsonify(dict)
