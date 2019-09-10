from sqlite3 import connect

class Database:

    def __init__(self, db):
        self.conn = connect(db)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, 
        title TEXT, author TEXT, year INTEGER, isbn INTEGER)
        """)
        self.conn.commit()

    def commit(self, query, values=()):
        self.cursor.execute(query, values)
        self.conn.commit()
        rows = self.cursor.fetchall()
        return rows


    def insert(self, title, author, year, isbn):
        query = """
        INSERT INTO books VALUES (NULL, ?, ?, ?, ?)
        """
        values = (title, author, year, isbn)
        self.commit(query, values)


    def view_all(self):
        query = """
        SELECT * FROM books
        """
        rows = self.commit(query)
        return rows


    def search(self, title="", author="", year="", isbn=""):
        query = """
        SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=?
        """
        values = (title, author, year, isbn)
        rows = self.commit(query, values)
        return rows


    def delete(self, ident):
        query = """
        DELETE FROM books WHERE id=?
        """
        values = (ident,)
        self.commit(query, values)


    def update(self, ident, title, author, year, isbn):
        query = """
        UPDATE books SET title=?, author=?, year=?, isbn=? WHERE id=?
        """
        values = (title, author, year, isbn, ident)
        self.commit(query, values)


    def __del__(self):      # executes on deleting object, i.e. exiting script
        self.conn.close()