from app.main import routes_bp
from flask import jsonify
from app.main.books import BOOKS

@routes_bp.route('/books', methods=["GET"])
def all_books():
    return jsonify({
        "status": "success",
        "books": BOOKS
    })
