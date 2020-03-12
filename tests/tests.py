import psycopg2
import sys

con = psycopg2.connect(host='localhost', database='postgres', user='postgres', password='postgres')

print(con.info)

path = sys.path

print(path[0])