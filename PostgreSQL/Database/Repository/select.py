import connection
from os import getenv
import sys
import utils


class Select:


    def __init__(self):
        self.db = getenv('PG_DATABASE')
        self.conn_string = getenv('CONN_STRING')


    def main(self):
        print("Select queries.")


    def find_all(options):
        try:
            if options['columns']:
                columns = utils.check_dynamic_column(options.columns)
                condition = utils.check_dynamic_condition(options['condition'])
            return ''
        except expression as identifier:
            pass


    def find_by_id(self):
        pass


    def find_one(self):
        pass


    def print_query(self):
        pass


if __name__ == "__main__":
    Select.main(True)