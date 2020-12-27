from sqlalchemy import func, select
from sqlalchemy.orm.attributes import InstrumentedAttribute
from models.Book import Book

from db import session


class BookController:

    def getAll(self):
        try:
            books = session.query(Book).all()
        except Exception as err:
            print(err)
        return books

    def createBook(self, name, desc, content):
        try:
            if isinstance(id, str) and isinstance(name, str) and isinstance(desc, str) and isinstance(content, str):
                raise Exception('Invalid arguments')
            b = Book(name, desc, content)
            session.add(b)
            session.commit()

        except Exception as err:
            print("Wrong data types! ", err)
            session.rollback()
            raise err

    def deleteBook(self, bookId):
        try:
            deletedItem = self.getById(bookId)
            if deletedItem is None: raise Exception('No book with such id')
            session.query(Book).filter(Book.id == bookId).delete()
            session.commit()
            return deletedItem
        except Exception as err:
            print("Delete error! ", err)
            session.rollback()
            raise err