# Importamos a biblioteca:
import init_mysql

def insert_query(conn):
    pass
    cursor = conn.cursor()
    res = cursor.execute(
        "INSERT INTO cars (plate, owner_name) VALUES ('ABC-1234', 'John'), ('ABC-1234', 'John')")
    print("Affected rows (Inserted): {}".format(res))
    conn.commit()

conn = init_mysql.open_connection()
insert_query(conn)
init_mysql.close_connection()