from addBook import addBook
from adminChecker import adminChecker
from connection import  Connection
from removeBook import RemoveBook
from showBooks import showBooks
from updateBook import updateBook


def main():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    adminCheck = adminChecker(username, password)
    adminResult = adminCheck.adminChecker()
    print(adminResult)
    if adminResult:
        while True:
            print("Hello admin!!")
            print("----------menu----------")
            print("[A] Show all books")
            print("[B] Add book")
            print("[C] Remove book")
            print("[D] Update book")
            print("[E] Exit")
            print("\n")
            choice = input("Enter your choice: ")
            match choice:
                case "A":
                    show = showBooks().showBookss()
                    print(show)

                case "B":
                    bookName = input("Enter book name : ")
                    isbn = input("Enter ISBN : ")
                    author = input(f"Enter author of {bookName} book: ")
                    if bookName and isbn and author:
                        addBook(bookName, isbn, author)
                    else:
                        print("Invalid input")
                case "C":
                    isbn = input("Enter ISBN for remove book : ")
                    RemoveBook(isbn)
                case "D":
                    isbn = input("Enter ISBN for update book : ")
                    updateBook(isbn)
                case "E":
                    print("Programme terminated!!")
                    break
                case __:
                    print("Invalid choice")
                    break










if __name__ == "__main__":
    main()





