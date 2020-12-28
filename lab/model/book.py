from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, PickleType
from sqlalchemy.ext.declarative import declarative_base

from lab.db import db


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
        return f'<Book name={self.name} \n' \
               f'Description = {self.description} \n' \
               f'>'