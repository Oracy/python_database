import query_select
import connection

conn = connection.create_connection('localhost', 'garage', 'postgres', 'postgres')

data = query_select.find_all(conn)

connection.close_connection(conn)

print(data)