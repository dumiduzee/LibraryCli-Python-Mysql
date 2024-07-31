from connection import Connection


class showBooks:
    def __init__(self):
        self.db = Connection()

    def showBookss(self):
       try:
           q = 'SELECT * FROM books'
           self.db.cursor.execute(q)
           books = self.db.cursor.fetchall()
           return books
       except Exception as e:
           return f"something went wrong {e}"