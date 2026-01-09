import psycopg2
def get_connection():
    return psycopg2.connect(
        database="mydatabase",
        user="furb-x",
        password="1234",
        host="localhost",
        port="5432"
    )

def create_table_authors():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS authors ("
        "id SERIAL PRIMARY KEY,"
        "full_name VARCHAR(100) NOT NULL,"
        "country VARCHAR(100) NOT NULL,"
    )
    conn.commit()
    cur.close()
    conn.close()