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

def delete_data(item):
    conn = sqlite3.connect('lite3.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM store WHERE item=?", (item,))
    conn.commit()
    conn.close()


def update_data(item, quantity, price):
    conn = sqlite3.connect('lite3.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE store SET quantity=?, price=? WHERE item=?", (quantity, price, item))
    conn.commit()
    conn.close()



if __name__ == "__main__":
    # create_table()
    # insert_data('Wine Glass', 5, 7)
    # insert_data('Water Glass', 10, 4)
    # insert_data('Cofee Cup', '3', '7')
    update_data('Wine Glass', 7, 10)