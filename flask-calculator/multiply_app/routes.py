from . import multiplication_bp
from flask import current_app as app, request, jsonify
from .multiply import multiply

@multiplication_bp.route('/multiply', methods=['GET'])
def add_route():
    num1 = int(request.args.get('num1', 0))
    num2 = int(request.args.get('num2', 0))
    result = multiply(num1, num2)
    return jsonify({'result': result})