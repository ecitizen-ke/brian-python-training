from flask import Blueprint, jsonify
products_bp = Blueprint('products_bp', __name__)


@products_bp.route('/products')
def get_products():
    dict = [{'fruits': ['apple', 'orange', 'banana']},
            {'drinks': ['tea', 'cofee', 'orange']}]
    return jsonify(dict)
