from app import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    title = db.Column(db.String(64))
    author = db.Column(db.String(64))
    read = db.Column(db.Boolean, default=False)

    def __repr(self):
        return "Book id: {}".format(self.id)