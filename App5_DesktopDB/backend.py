from sqlite3 import connect


def commit(query, values=()):
    conn = connect("bookshelf.db")
    cursor = conn.cursor()
    cursor.execute(query, values)
    conn.commit()
    rows = cursor.fetchall()
    conn.close()
    return rows

def create_table():
    query = """
    CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, 
    title TEXT, author TEXT, year INTEGER, isbn INTEGER)
    """
    commit(query)


def insert(title, author, year, isbn):
    query = """
    INSERT INTO books VALUES (NULL, ?, ?, ?, ?)
    """
    values = (title, author, year, isbn)
    commit(query, values)


def view_all():
    query = """
    SELECT * FROM books
    """
    rows = commit(query)
    return rows


def search(title="", author="", year="", isbn=""):
    query = """
    SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=?
    """
    values = (title, author, year, isbn)
    rows = commit(query, values)
    return rows


def delete(ident):
    query = """
    DELETE FROM books WHERE id=?
    """
    values = (ident,)
    commit(query, values)


def update(ident, title, author, year, isbn):
    query = """
    UPDATE books SET title=?, author=?, year=?, isbn=? WHERE id=?
    """
    values = (title, author, year, isbn, ident)
    commit(query, values)
