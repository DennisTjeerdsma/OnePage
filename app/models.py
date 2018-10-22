from app import db, marshmallow


class BookSchema(marshmallow.Schema):
    class Meta:
        fields = ("title", "author", "read")


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    title = db.Column(db.String(64))
    author = db.Column(db.String(128))
    read = db.Column(db.Boolean, default=False)

    def __repr(self):
        return "Book id: {}".format(self.id)

    @staticmethod
    def book_dict_list():
        book_list = Book.query.all()
        bookschema = BookSchema(many=True)
        book_dict = bookschema.dump(book_list)
        return book_dict
