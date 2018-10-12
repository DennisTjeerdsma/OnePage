from flask import jsonify
from app.main import routes_bp

@routes_bp.route("/", methods=["GET"])
@routes_bp.route("/home", methods=["GET"])
def index():
    return jsonify("Poep")