from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, PickleType
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class Reader(Base):
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


    def __init__(self, name: str, password: str, role="user"):
        self.username = name
        self.password = password
        self.role = role

    def __repr__(self):
        return f'<Reader username= {self.username}' \
               f'role = {self.role}' \
               f'>'
