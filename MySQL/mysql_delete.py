import pymysql

conn = pymysql.connect(db='garage', user='root', passwd='')

cursor = conn.cursor()
res = cursor.execute("DELETE FROM cars WHERE plate = 'ABC-1234'")
print("Affected rows (Deleted): {}".format(res))

conn.commit()
conn.close()
