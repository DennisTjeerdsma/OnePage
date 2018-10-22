from app.main import routes_bp
from app.models import Book
from flask import request, jsonify
from removebook import remove_book

@routes_bp.route("/books/<book_id>", methods=["PUT"])
def update_book(book_id):
    response_object = {"status": "succes"}
    if request.method == "PUT":
        remove_book(book_id)
        add_book = Book(
            title=request.json.get("title", ""),
            author=request.json.get("author", ""),
            read=request.json.get("read", "")
        )
        response_object["message"] = "Book added!"
    else:
        response_object["books"] = Book.book_dict_list().data
    return jsonify(response_object)

    