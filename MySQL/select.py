import mysql


def main():
    print("Function to work just getting data.")


def check_dynamic_column(columns):
    columns = "*" if columns == None else columns
    return columns


def check_dynamic_condition(condition):
    condition = "1=1" if condition == None else condition
    return condition


def find_all(conn, columns=None, condition=None, limit=None):
    columns = check_dynamic_column(columns)
    condition = check_dynamic_condition(condition)
    conn.execute(
        "SELECT {} FROM cars WHERE 1=1 AND {}".format(columns, condition))
    if limit == None:
        return conn.fetchall()
    else:
        return conn.fetchmany(size=limit)


def find_by_id(conn, id, columns=None):
    columns = check_dynamic_column(columns)
    conn.execute(
        "SELECT {} FROM cars WHERE 1=1 AND {}".format(columns, id))
    return conn.fetchall()


def find_one(conn, columns=None, condition=None):
    columns = check_dynamic_column(columns)
    condition = check_dynamic_condition(condition)
    conn.execute(
        "SELECT {} FROM cars WHERE {}".format(columns, condition))
    return conn.fetchmany(size=1)


# def print_query(data):
#     print('Query result: ')
#     for linha in data:
#         print('---------------------------------')
#         print('Id = {}'.format(linha[0]))
#         print('Car owner = {}'.format(linha[2]))
#         print('Car plate = {}'.format(linha[1]))
#     print("\nTotal Find: {}".format(len(data)))


# conn = mysql.open_connection().cursor()
# data = find_all(conn, limit=5)
# data = find_one(conn)
# data = find_by_id(conn, 'id=16')
# print_query(data)
# mysql.close_connection(conn)


if __name__ == "__main__":
    main()
