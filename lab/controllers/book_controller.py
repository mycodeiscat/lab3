from lab.model import Book
from lab.model import book_author
from lab.db import db


class BookController:

    def getAll(self):
        try:
            books = db.session.query(Book).all()
        except Exception as err:
            print(err)
        return books

    def createBook(self, name, desc, content):
            try:
                if isinstance(id, str) and isinstance(name, str) and isinstance(desc, str) and isinstance(content, str):
                    raise Exception('Invalid arguments')
                b = Book(name=name, description=desc, content=content)
                db.session.add(b)
                db.session.commit()
                db.session.refresh(b)
                return b
            except Exception as err:
                print("Wrong data types! ", err)
                db.session.rollback()
                raise err

    def deleteBook(self, bookId):
        try:
            deletedItem = self.getById(bookId)
            if deletedItem is None: raise Exception('No book with such id')
            db.session.query(Book).filter(Book.id == bookId).delete()
            db.session.commit()
            return deletedItem
        except Exception as err:
            print("Delete error! ", err)
            db.session.rollback()
            raise err

    def updateBook(self, bookId, name, desc, content):
        try:
            book = db.session.query(Book).get(bookId)
            book.name = name
            book.description = desc
            book.content = content
            db.session.add(book)
            db.session.commit()
        except Exception as err:
            print(err)
            raise err
        return book

    def getById(self, bookId):
        try:
            book = db.session.query(Book).get(bookId)
        except Exception as err:
            print(err)
            raise err
        return book

