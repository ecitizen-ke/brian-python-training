from flask import Blueprint
subtraction_bp = Blueprint('subtraction_bp', __name__)
from . import routes
