import pymysql


def main():
    print('Handle Mysql connections')


def open_connection():
    return pymysql.connect(db='garage', user='root', passwd='')


def close_connection(conn):
    conn.close()


if __name__ == "__main__":
    main()