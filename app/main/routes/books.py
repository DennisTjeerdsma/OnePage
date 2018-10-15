from app.main import routes_bp
from flask import jsonify, request
from app.models import Book
from app import db


@routes_bp.route('/books', methods=['GET', 'POST'])
def all_books():
    response_object = {"status": "success"}
    if request.method == "POST":
        add_book = Book(title=request.json.get("title", ""),
                        author=request.json.get("author", ""),
                        read=request.json.get("read", "")
                        )
        db.session.add(add_book)
        db.session.commit()
        response_object["message"] = "Book added!"
    else:
        response_object["books"] = BOOKS
    return jsonify(response_object)