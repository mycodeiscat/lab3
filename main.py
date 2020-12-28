from lab.app import app
from lab.db import db
import os

from lab.db.fixtures import seed_db


def drop_all_tables(app):
    db.engine.execute("DROP SCHEMA public CASCADE")
    db.engine.execute("CREATE SCHEMA public")


def recreate_db():
    drop_all_tables(app=app)
    db.create_all(app=app)

    seed_db()


if __name__ == "__main__":
    with app.app_context():
        recreate_db()
        print("f")
        from lab.controllers.book_controller import BookController
        from lab.controllers.author_controller import AuthorController
        from lab.controllers.reader_controller import ReaderController
        books = BookController()
        authors = AuthorController()
        readers = ReaderController()
        while True:
            # os.system('clear')
            print("1. Books")
            print("2. Authors")
            print("3. Readers")
            choice = input()
            if choice == "1":
                print("Books")
                print("1. Create")
                print("2. Update")
                print("3. Delete")
                print("4. Show all")
                print("5. Get Book by id")
                choice = input()
                if choice == "1":
                    name = input()
                    desc = input()
                    content = input()
                    b = books.createBook(name, desc, content)
                    print("Author id")
                    aid = input()
                    if aid:
                        author = authors.getById(aid)
                        if author:
                            author.books.append(b)
                if choice == "2":
                    bid = input()
                    name = input()
                    desc = input()
                    content = input()
                    books.updateBook(bid, name, desc, content)
                if choice == "3":
                    book_id = input()
                    books.deleteBook(book_id)
                if choice == "4":
                    info = books.getAll()
                    for item in info:
                        print(item)
                if choice == "5":
                    bid = input()
                    book = books.getById(bid)
                    print(book)
            if choice == "2":
                print("Auhors")
                print("1. Create")
                print("2. Update")
                print("3. Delete")
                print("4. Show all")
                print("5. Get author by id")
                choice = input()
                if choice == "1":
                    name = input()
                    bio = input()
                    authors.createAuthor(name, bio)
                if choice == "2":
                    aid = input()
                    name = input()
                    bio = input()
                    authors.updateAuthor(aid, name, bio)
                if choice == "3":
                    rid = input()
                    authors.deleteAuthor(rid)
                if choice == "4":
                    info = authors.getAll()
                    for item in info:
                        print(item)
                if choice == "5":
                    rid = input()
                    author = authors.getById(rid)
                    print(author)
            if choice == "3":
                print("Readers")
                print("1. Create")
                print("2. Update")
                print("3. Delete")
                print("4. Show all")
                print("5. Get reader by id")
                choice = input()
                if choice == "1":
                    name = input()
                    password = input()
                    readers.createReader(name, password)
                if choice == "2":
                    rid = input()
                    name = input()
                    password = input()
                    role = input()
                    readers.updateReader(rid, name, password, role)
                if choice == "3":
                    rid = input()
                    readers.deleteReader(rid)
                if choice == "4":
                    info = readers.getAll()
                    for item in info:
                        print(item)
                if choice == "5":
                    rid = input()
                    reader = readers.getById(rid)
                    print(reader)
            if choice == "0":
                break
