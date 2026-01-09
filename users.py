import psycopg2
def get_connection():
    return psycopg2.connect(
        database="mydatabase",
        user="furb-x",
        password="1234",
        host="localhost",
        port="5432"
    )


def create_table_users():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(""" CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    e-mail VARCHAR(100) NOT NULL,
    password  TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL,
    );
    FOREIGN KEY (full_name) REFERENCES users (id);
    """)
    conn.commit()
    cur.close()
    conn.close()



