#!/usr/bin/python3
import MySQLdb
db = MySQLdb.connect(host="localhost", user="root", db="hbtn_0e_0_usa")
cur = db.cursor()
cur.execute("SELECT * FROM states ORDER BY name ASC")
result = cur.fetchall()
for row in result:
    print("{}".format(row))
cur.close()
db.close()
