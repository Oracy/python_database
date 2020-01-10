import pymysql

conn = pymysql.connect(db='garage', user='root', passwd='')

cursor = conn.cursor()
res = cursor.execute(
    "UPDATE cars SET owner_name = 'Joseph' WHERE plate = 'ABC-1234'")
print("Affected rows (Updated): {}".format(res))

conn.commit()
conn.close()
