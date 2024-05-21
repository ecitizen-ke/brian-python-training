from . import addition_bp
from flask import current_app as app, request, jsonify
from .add import add

@addition_bp.route('/add', methods=['GET'])
def add_route():
    num1 = int(request.args.get('num1', 0))
    num2 = int(request.args.get('num2', 0))
    result = add(num1, num2)
    return jsonify({'result': result})
