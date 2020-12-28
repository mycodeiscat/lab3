from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, PickleType
from lab.db import db


class Author(db.Model):
    id = Column(
        Integer,
        primary_key=True,
        nullable=False
    )

    name = Column(
        String(100),
        nullable=False
    )
    bio = Column(
        Text,
        nullable=True
    )

    books = db.relationship("Book", secondary="book_author")

    def __repr__(self):
        return f'<Author name={self.name} \n' \
               f'bio = {self.bio} \n' \
               f'>'
