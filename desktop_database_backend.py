import sqlite3

db_name = 'book_catalogue.db'

def create_table():
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, author TEXT, year INTEGER, title TEXT, isbn INTEGER)')
    conn.commit()
    conn.close()


def add_record(author='', year='', title='', isbn=''):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute(f'INSERT INTO books VALUES (NULL, "{author}", {year}, "{title}", {isbn})')
    conn.commit()
    conn.close()


def view_records():
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute('SELECT * FROM books')
    datos = cur.fetchall()
    conn.close()
    return datos


def search_record(author='', year='', title='', isbn=''):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute(f'SELECT * FROM books WHERE author = "{author}" OR year = "{year}" OR title = "{title}" OR isbn = "{isbn}"')
    libro = cur.fetchall()
    conn.close()
    return libro


def update_record(id, author, year, title, isbn):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute(f'UPDATE books SET author = "{author}", year = {year}, title = "{title}", isbn = {isbn} WHERE id = {id}')
    conn.commit()
    conn.close()


def delete_record(id):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute(f'DELETE FROM books WHERE id = {id}')
    conn.commit()
    conn.close()


def delete_all():
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute('DELETE FROM books')
    conn.commit()
    conn.close()


create_table()
