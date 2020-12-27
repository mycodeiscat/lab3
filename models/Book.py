from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, PickleType
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
# from models.links import link_reader_book
Ы

Base = declarative_base()


class Book(Base):
    __tablename__ = "Book"

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

    def __init__(self, name: str, desc: str, content):
        self.name = name
        self.description = desc
        self.content = content

    def __repr__(self):
        return f'<Book name= {self.name}' \
               f'description = {self.description}' \
               f'>'
