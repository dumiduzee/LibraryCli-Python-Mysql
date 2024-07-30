from connection import Connection


class adminChecker:
    def __init__(self,username,password):
        self.db = Connection()
        self.username = username
        self.password = password



    def adminChecker(self):
        try:
            q = f'SELECT * FROM admin WHERE name="{self.username}" and password="{self.password}"'
            self.db.cursor.execute(q)
            result = self.db.cursor.fetchall()
            if result:
                return True
            else:
                print("error")
                return False
        except Exception as e:
            print(f"Something went wrong {e}")
