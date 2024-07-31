from connection import Connection


class addBook:
    def __init__(self,name,author,isbn):
        self.name = name
        self.author = author
        self.isbn = isbn
        self.db = Connection()
        try:
            q = f'insert into books (name,author,isbn) values ("{self.name}","{self.author}","{self.isbn}")'
            self.db.cursor.execute(q)
            self.db.commits()
            print(f"{self.name} Added to library success!!!")
        except Exception as e:
            print(f"something went wrong {e}")


