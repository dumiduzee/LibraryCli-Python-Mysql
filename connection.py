
class Connection:
    import mysql.connector
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="4878",
        database="library"
    )
    cursor = db.cursor()
