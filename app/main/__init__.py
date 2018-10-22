from flask import Blueprint

routes_bp = Blueprint("routes_bp", __name__)

from app.main.routes import index
from app.main.routes import books
from app.main.routes import updatebook

