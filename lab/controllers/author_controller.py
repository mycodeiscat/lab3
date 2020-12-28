from lab.model import Author

from lab.db import db


class AuthorController:

    def getAll(self):
        try:
            authors = db.session.query(Author).all()
        except Exception as err:
            print(err)
        return authors

    def createAuthor(self, name, bio):
        try:
            if isinstance(id, str) and isinstance(name, str) and isinstance(bio, str):
                raise Exception('Invalid arguments')
            b = Author(name=name, bio=bio)
            db.session.add(b)
            db.session.commit()

        except Exception as err:
            print("Wrong data types! ", err)
            db.session.rollback()
            raise err

    def deleteAuthor(self, authorId):
        try:
            deletedItem = self.getById(authorId)
            if deletedItem is None: raise Exception('No author with such id')
            db.session.query(Author).filter(Author.id == authorId).delete()
            db.session.commit()
            return deletedItem
        except Exception as err:
            print("Delete error! ", err)
            db.session.rollback()
            raise err

    def updateAuthor(self, authorId, name, bio):
        try:
            author = db.session.query(Author).get(authorId)
            author.name = name
            author.bio = bio
            db.session.add(author)
            db.session.commit()
        except Exception as err:
            print(err)
            raise err
        return author

    def getById(self, authorId):
        try:
            author = db.session.query(Author).get(authorId)
        except Exception as err:
            print(err)
            raise err
        return author
