import psycopg2

con = psycopg2.connect(host='localhost', database='postgres', user='postgres', password='postgres')

print(con.info)