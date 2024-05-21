from flask import Blueprint
multiplication_bp = Blueprint('multiplication_bp', __name__)
from . import routes