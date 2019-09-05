import sqlite3


def create_table():
    conn = sqlite3.connect('lite3.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()
   

def insert_data(item, quantity, price):
    conn = sqlite3.connect('lite3.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO store VALUES(?, ?, ?)", (item, quantity, price))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_table()
    insert_data('Water Glass', 10, 4)
    insert_data('Cofee Cup', '3', '7')