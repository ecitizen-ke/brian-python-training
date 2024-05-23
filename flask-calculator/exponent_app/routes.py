from . import exponential_bp
from flask import current_app as app, request, jsonify
from .exponent import exponent


@exponential_bp.route('/exponent', methods=['GET'])
def exponent_route():
    num1 = int(request.args.get('num1', 0))
    num2 = int(request.args.get('num2', 0))
    result = exponent(num1, num2)
    return jsonify({'result': result})
