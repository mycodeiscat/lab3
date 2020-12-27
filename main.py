from controllers.BookController import BookController
from db import session, recreate_database

from models.Author import Author
from models.Reader import Reader

# recreate_database()

if __name__ == "__main__":
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
