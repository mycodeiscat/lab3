from lab.model import Reader

from lab.db import db


class ReaderController:

    def getAll(self):
        try:
            readers = db.session.query(Reader).all()
        except Exception as err:
            print(err)
        return readers

    def createReader(self, username, password, role="user"):
        try:
            if isinstance(id, str) and isinstance(username, str) and isinstance(password, str):
                raise Exception('Invalid arguments')
            b = Reader(name=username, password=password, role=role)
            db.session.add(b)
            db.session.commit()

        except Exception as err:
            print("Wrong data types! ", err)
            db.session.rollback()
            raise err

    def deleteReader(self, readerId):
        try:
            deletedItem = self.getById(readerId)
            if deletedItem is None: raise Exception('No reader with such id')
            db.session.query(Reader).filter(Reader.id == readerId).delete()
            db.session.commit()
            return deletedItem
        except Exception as err:
            print("Delete error! ", err)
            db.session.rollback()
            raise err

    def updateReader(self, readerId, name, password, role):
        try:
            reader = db.session.query(Reader).get(readerId)
            reader.username = name
            reader.password = password
            reader.role = role
            db.session.add(reader)
            db.session.commit()
        except Exception as err:
            print(err)
            raise err
        return reader

    def getById(self, readerId):
        try:
            reader = db.session.query(Reader).get(readerId)
        except Exception as err:
            print(err)
            raise err
        return reader
