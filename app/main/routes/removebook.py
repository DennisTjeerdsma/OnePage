from app.models import Book
from app import db


def remove_book(book_id):
    u = Book.query.filter_by(id=book_id).first_or_404()
    if u:
        db.session.remove(u)
        return True
    return False
