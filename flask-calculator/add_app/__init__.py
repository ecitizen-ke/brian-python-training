from flask import Blueprint
addition_bp = Blueprint('addition_bp', __name__)
from . import routes
