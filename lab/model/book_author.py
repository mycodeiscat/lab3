from sqlalchemy import Integer, ForeignKey

from lab.db import db


class BookAuthor(db.Model):
    id = db.Column(
        Integer,
        primary_key=True,
    )

    author_id = db.Column(
        Integer, ForeignKey("author.id", on_delete="CASCADE"), nullable=False
    )
    book_id = db.Column(
        Integer, ForeignKey("book.id", on_delete="CASCADE"), nullable=False
    )
