from flask import Blueprint, jsonify

index_bp = Blueprint('index_bp', __name__, )


@index_bp.route('/')
def index():
    return '<h1> hello, world! </h1>'
