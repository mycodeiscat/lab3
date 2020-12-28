from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, PickleType, ForeignKey
from lab.db import db


class Reader(db.Model):
    __tablename__ = "Reader"

    id = Column(
        Integer,
        primary_key=True,
        nullable=False
    )

    username = Column(
        String(100),
        nullable=False
    )

    password = Column(
        String(64),
        nullable=False
    )

    role = Column(
        String(32),
        nullable=False
    )

    book_id = db.Column(Integer, ForeignKey("book.id", ondelete="SET NULL"))
    book = db.relationship("Book", back_populates="readers")

    def __repr__(self):
        return f'<Reader username= {self.username}' \
               f'role = {self.role}' \
               f'>'
