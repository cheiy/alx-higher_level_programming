#!/usr/bin/python3
import MySQLdb
if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user="root", port=3306, passwd="roo\
                         t", db="hbtn_0e_0_usa")
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    result = cur.fetchall()
    for row in result:
        print("{}".format(row))
    cur.close()
    db.close()
