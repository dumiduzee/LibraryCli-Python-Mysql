
class Connection:
    import mysql.connector
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="4878",
        database="library"
    )
    cursor = db.cursor()
    commit = db.commit()

    def commits(self):
        return self.db.commit()
