import pprint

from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, PickleType
from lab.db import db
from lab.util.schemas import ReaderSchema, BookSchema


class Book(db.Model):
    id = Column(
        Integer,
        primary_key=True,
    )

    name = Column(
        String(100),
        nullable=False
    )

    description = Column(
        Text,
        nullable=True
    )

    content = Column(
        Text,
        nullable=False
    )

    authors = db.relationship("Author", secondary="book_author")

    readers = db.relationship("Reader", back_populates="book")

    def __repr__(self):
        return pprint.pformat(BookSchema().dump(self), indent=4)
