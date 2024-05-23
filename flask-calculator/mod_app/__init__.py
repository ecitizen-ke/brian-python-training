from flask import Blueprint
modulo_bp = Blueprint('modulo_bp', __name__)
from . import routes
