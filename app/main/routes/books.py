from app.main import routes_bp
from flask import jsonify, request
from app.main.booklist import BOOKS


@routes_bp.route('/books', methods=['GET', 'POST'])
def all_books():
    return jsonify({
        'status': 'success',
        'books': BOOKS
    })
