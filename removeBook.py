from connection import Connection


class RemoveBook:
    def __init__(self, isbn):
        self.isbn = isbn
        self.db = Connection()
        try:

                q = f'DELETE FROM books WHERE isbn="{self.isbn}"'
                print(q)
                self.db.cursor.execute(q)
                self.db.commits()
                print("Book has been removed")
        except Exception as e:
            print(f"Error: {e}")
