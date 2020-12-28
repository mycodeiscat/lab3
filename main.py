from lab.app import app
from lab.db import db


def drop_all_tables(app):
    db.engine.execute("DROP SCHEMA public CASCADE")
    db.engine.execute("CREATE SCHEMA public")


def recreate_db():
    drop_all_tables(app=app)
    db.create_all(app=app)




if __name__ == "__main__":
    with app.app_context():
        recreate_db()
        print("f")
        from lab.controllers.book_controller import BookController
        books = BookController()
        while True:
            print("1. Books")
            choice = input()
            if choice == "1":
                print("Books")
                print("1. Create")
                print("2. Update")
                print("3. Delete")
                print("4. Show all")
                choice = input()
                if choice == "1":
                    name = input()
                    desc = input()
                    content = input()
                    books.createBook(name, desc, content)
                if choice == "3":
                    book_id = input()
                    books.deleteBook(book_id)
                if choice == "4":
                    info = books.getAll()
                    for item in info:
                        print(item)
            if choice == "0":
                break
