import psycopg2

class Connection(object):
    _db=None
    def __init__(self, pghost, db, usr, pwd):
        self._db = psycopg2.connect(
            host=pghost, database=db, user=usr, password=pwd)


def main():
    print("Manage Connections")


def create_connection(host, database, user, password):
    conn = psycopg2.connect(host=host, database=database,
                           user=user, password=password)
    return conn.cursor()


def close_connection(conn):
    conn.close()


if __name__ == "__main__":
    main()
