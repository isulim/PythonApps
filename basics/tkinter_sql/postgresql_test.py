import psycopg2


def connect():
    return psycopg2.connect("dbname='psqldb' user='postgres' password='74985632aA!#' host='localhost' port='5432'")

def create_table():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()
   

def insert_data(item, quantity, price):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO store VALUES(%s, %s, %s)", (item, quantity, price))
    conn.commit()
    conn.close()

def delete_data(item):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM store WHERE item=%s", (item,))
    conn.commit()
    conn.close()


def update_data(item, quantity, price):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))
    conn.commit()
    conn.close()



if __name__ == "__main__":
    create_table()
    # insert_data('Wine Glass', 5, 7)
    # insert_data('Water Glass', 10, 4)
    # insert_data('Cofee Cup', '3', '7')
    update_data('Wine Glass', 7, 10)