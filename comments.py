import psycopg2
def get_connection():
    return psycopg2.connect(
        database="mydatabase",
        user="furb-x",
        password="1234",
        host="localhost",
        port="5432",
    )

def create_table_comments():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS comments (
    id SERIAL PRIMARY KEY,
    user_id INTEGER,
    book_id INTEGER,
    content TEXT,
    created_at TIMESTAMP,
    FOREIGN KEY (author_id) REFERENCES authors (id),
    FOREIGN KEY (book_id) REFERENCES books (id)
    );
    """)
    conn.commit()
    cur.close()
    conn.close()