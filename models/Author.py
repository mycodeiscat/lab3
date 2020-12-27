from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, PickleType
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
# from models.links import link_reader_book

Base = declarative_base()


class Author(Base):
    __tablename__ = "Author"

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

    #Books = relationship("Book", secondary=link_reader_book, cascade="all, delete")

    def __init__(self, name: str, bio: str):
        self.name = name
        self.bio = bio

    def __repr__(self):
        return f'<Author name= {self.name}' \
               f'bio = {self.bio}' \
               f'>'
