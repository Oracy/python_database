import psycopg2
from os import getenv


class Database:

    conn_string = ''
    db = ''

    def __init__(self):
        self.db = getenv('PG_DATABASE')
        self.conn_string = getenv('CONN_STRING')

    def connect(self, options):
        try:
            self.client = psycopg2.connect(
                host=options['dbhost'], database=options['db'], user=options['usr'], password=options['pwd'])
            self.client.info
        except Exception as error:
            raise Exception(
                'There was an error while trying to connect to database: {}'.format(error))

    def disconnect(self):
        self.client.close()
        self.client = None

    def main(self):
        print("Manage Connections")


if __name__ == "__main__":
    Database.main(True)
