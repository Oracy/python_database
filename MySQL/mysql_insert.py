import init_mysql

def insert_query(conn, table=None, columns=None, data=None):
    cursor = conn.cursor()
    res = cursor.execute(
        "INSERT INTO {} ({}) VALUES {}")
    print("Affected rows (Inserted): {}".format(res))
    conn.commit()

conn = init_mysql.open_connection()
insert_query(conn)
init_mysql.close_connection(conn)