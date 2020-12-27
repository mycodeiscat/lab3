from sqlalchemy import Column, Integer, Table, ForeignKey
from db import Base

link_book_author = Table(
    'BookAuthor', Base.metadata,
    Column('bookId', Integer, ForeignKey('Book.id')),
    Column('authorId', Integer, ForeignKey('Author.id'))
)


