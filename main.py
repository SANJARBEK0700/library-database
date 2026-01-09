import psycopg2
from prettytable import PrettyTable
import users
import authors
import genres

def get_connection():
    return psycopg2.connect(
        dbname="mydatabase",
        user="furb-x",
        password="1234",
        host="localhost",
        port=5432
    )

def create_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(""" CREATE TABLE IF NOT EXISTS books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(150),
    author_id INTEGER,
    published_year INTEGER,
    genre_id INTEGER,
    created_at TIMESTAMP,
    FOREIGN KEY (author_id) REFERENCES authors (id),
    FOREIGN KEY (genre_id) REFERENCES genres (id)
    );
    """)
    conn.commit()
    cur.close()
    conn.close()


def insert_book():
    conn = get_connection()
    cur = conn.cursor()
    name = input("Insert book name: ")
    published_year = input("Insert published year: ")
    created_at = input("Insert published date: ")
    cur.execute("INSERT INTO books (title, published_year, created_at) VALUES (%s, %s, %s)", (name, published_year, created_at))
    conn.commit()
    cur.close()
    conn.close()

def get_books():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM books;")
    rows = cur.fetchall()
    columns = [i[0] for i in cur.description]

    table = PrettyTable()
    table.field_names = columns
    table.add_rows(rows)

    print(table)


def delete_book():
    conn = get_connection()
    cur = conn.cursor()
    book_id = input("Insert book id that you want to delete: ")
    cur.execute("DELETE FROM books WHERE id = %s", (book_id,))
    conn.commit()
    cur.close()
    conn.close()

def update_book():
    conn = get_connection()
    cur = conn.cursor()
    book_id = input("Insert book id that you want to update: ")
    title = input("Insert new book title: ")
    author = input("Insert new book author: ")
    country = input("Insert new book country: ")
    cur.execute("UPDATE books SET title = %s, author = %s, country = %s WHERE id = %s", (title , author, country, book_id))
    conn.commit()
    cur.close()
    conn.close()

def book_search():
    conn = get_connection()
    cur = conn.cursor()
    name = input("Insert book name: ")
    cur.execute("SELECT * FROM books (name) WHERE title = %s", (name,))
    rows = cur.fetchall()


    if rows:
        table = PrettyTable()
        table.field_names = [i[0] for i in cur.description]
        table.add_rows(rows)
        print(table)
    else:
        print("Book not found!")

def author_search():
    conn = get_connection()
    cur = conn.cursor()
    name = input("Insert author: ")
    cur.execute("SELECT * FROM authors (full_name) WHERE name = %s", (name,))

def genre_search():
    conn = get_connection()
    cur = conn.cursor()
    name = input("Insert genre: ")
    cur.execute("SELECT * FROM genres (name) WHERE name = %s", (name,))


def user_search():
    conn = get_connection()
    cur = conn.cursor()
    name = input("Insert user name: ")
    cur.execute("SELECT * FROM users (full_name) WHERE name = %s", (name,))

def menu():
    print("""
    ===========    Main Menu ===========
    1. Add book
    2. Search book
    3. Delete book
    4. Update book
    5. Search author
    6. Search genre
    7. Search user
    8. Exit
    ====================================
    """)

if __name__ == "__main__":
    create_table()
    while True:
        menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            insert_book()
        elif choice == "2":
            book_search()
        elif choice == "3":
            delete_book()
        elif choice == "4":
            update_book()
        elif choice == "5":
            author_search()
        elif choice == "6":
            genre_search()
        elif choice == "7":
            user_search()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Wrong Command")