# Imports
import os
import unittest
from flask import Flask
from config import basedir
from personal import app, db
from app.models import Book


class TestCase(unittest.TestCase):
    ##########################
    ### Setup and Teardown ###
    ##########################

    # Executed before test
    def setUp(self):
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "test.db")
        app.config["DEBUG"] = False
        app.config["WTF_CSRF_ENABLED"] = False
        self.app = app.test_client()
        ctx = app.app_context()
        ctx.push()
        db.create_all()

    # executed after each test
    def tearDown(self):
        db.session.remove()
        db.drop_all()

    ###########
    ## Tests ##
    ###########

    # Tests if book gets properly stored to the database
    def test_book_add(self):
        u = Book(author="Brandon Sanderson", title="Oathbreaker", read=True)
        db.session.add(u)
        db.session.commit()

        x = Book.query.get(1)
        all_book = Book.query.count()

        self.assertEqual(x.title, u.title)
        self.assertEqual(x.author, u.author)
        self.assertEqual(x.read, u.read)
        self.assertNotEqual(x.read, False)
        self.assertEqual(all_book, 1)


if __name__== "__main__":
    unittest.main()
    


