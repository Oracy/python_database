import init_mysql

def select_query(conn, columns=None, condition=None):
    cursor = conn.cursor()
    columns = "*" if columns == None else columns
    condition = "1=1" if condition == None else condition
    cursor.execute("SELECT {} FROM cars WHERE 1=1 AND {}".format(columns, condition))
    # data = cursor.fetchmany(size=5)
    return cursor.fetchall()


def print_query(data):
    print('Query result: ')
    for linha in data:
        print('---------------------------------')
        print('Id = {}'.format(linha[0]))
        print('Car owner = {}'.format(linha[2]))
        print('Car plate = {}'.format(linha[1]))
    print("\nTotal Find: {}".format(len(data)))


conn = init_mysql.open_connection()
data = select_query(conn)
print_query(data)
init_mysql.close_connection(conn)
