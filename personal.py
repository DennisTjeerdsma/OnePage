from app import create_app, db
from app.models import Book

#Creating app
app = create_app()

#Initializing shell
@app.shell_context_processor
def make_shell_context():
    return{"db": db, "Book": Book}
