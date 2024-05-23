from flask import Blueprint
exponential_bp = Blueprint('exponential_bp', __name__)
from . import routes