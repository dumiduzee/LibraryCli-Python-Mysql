from connection import Connection
class updateBook:
    def __init__(self,isbn):
        self.isbn = isbn
        self.db = Connection()
        try:
            self.newName = input("Enter new name for book : ")
            self.newIsbn = input("Enter new isbn to book : ")
            self.newAuthor = input("Enter new author of book : ")
            q = f'UPDATE books SET isbn = "{self.newIsbn}", author = "{self.newAuthor}",name = "{self.newName}" WHERE isbn = "{self.isbn}"'
            print(q)
            self.db.cursor.execute(q)
            self.db.db.commit()
            print("Data updated success!!")
        except Exception as e:
            print(e)


