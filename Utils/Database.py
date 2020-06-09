"""
Crud operation with sqlite
format OOP - API
"""

from Utils import Database_Manager



print('####################################'.strip())
print(__doc__.strip())
print("####################################")



def create_database_table():
    with Database_Manager.databaseContextManager('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('CREATE TABLE IF NOT EXISTS books_db(name text primary key, author text, read text);')

def add_book( name, author):
    with Database_Manager.databaseContextManager('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('INSERT OR IGNORE INTO books_db VALUES(?,?,0);', (name, author))

def get_all_books():
    with Database_Manager.databaseContextManager('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM books_db;')
        books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]
    return books

def mark_book_as_read( name):
    with Database_Manager.databaseContextManager('data.db') as connection:
        cursor = connection.cursor()

        sql = """UPDATE books_db SET read = 1 WHERE name = ?"""
        val = (name,)
        cursor.execute(sql, val)
        # cursor.execute('SELECT * FROM books_db')
        # record_updated = cursor.fetchone()
        # print(record_updated)

def delete_book( name):
    with Database_Manager.databaseContextManager('data.db') as connection:
        cursor = connection.cursor()
        sql = """DELETE FROM books_db WHERE name = ?"""
        val = (name,)
        cursor.execute(sql, val)
        # # After deleting the record we print it
        # cursor.execute('SELECT * FROM books_db')
        # record_deleted = cursor.fetchone()
        # print(record_deleted)
