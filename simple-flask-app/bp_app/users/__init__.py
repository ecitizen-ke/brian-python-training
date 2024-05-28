from flask import Blueprint, jsonify
users_bp = Blueprint('users_bp', __name__)


@users_bp.route('/users')
def get_users():
    dict = [{'username': 'admin', 'password': 'admin123'},
            {'username': 'brian', 'password': 'brian123'}
            ]
    return jsonify(dict)
