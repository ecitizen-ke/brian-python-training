from . import modulo_bp
from flask import current_app as app, request, jsonify
from .mod import mod


@modulo_bp.route('/mod', methods=['GET'])
def add_route():
    num1 = int(request.args.get('num1', 0))
    num2 = int(request.args.get('num2', 0))
    result = mod(num1, num2)
    return jsonify({'result': result})
