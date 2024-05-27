from flask import Blueprint, render_template

home_bp = Blueprint('home_bp', __name__, template_folder='templates')


@home_bp.route('/')
def index():
    return render_template('index.html')


# @home_bp.route('/hello')
# def hello():
#     return 'hello world'


# @home_bp.route('/hello/<name>')
# def hello_name(name):
#     return f'hello{name}'
