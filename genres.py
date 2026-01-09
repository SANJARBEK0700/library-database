import psycopg2
def get_connection():
    return psycopg2.connect(
        database="mydatabase",
        user="furb-x",
        password="1234",
        host="localhost",
        port="5432"
    )

def create_table_genres():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS genres (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL
    );
    """)
    conn.commit()
    cur.close()
    conn.close()