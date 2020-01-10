import connection
import utils

def main():
    print("Select queries.")


def find_all(conn, columns=None, condition=None, limit=None):
    columns = utils.check_dynamic_column(columns)
    condition = utils.check_dynamic_condition(condition)
    conn.execute(
        "SELECT {} FROM cars WHERE 1=1 AND {}".format(columns, condition))
    if limit == None:
        return conn.fetchall()
    else:
        return conn.fetchmany(size=limit)


def find_by_id():
    return ''


def find_one():
    return ''


def print_query():
    return ''


if __name__ == "__main__":
    main()
