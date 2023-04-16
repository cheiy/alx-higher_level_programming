#!/usr/bin/python3
import MySQLdb
if __name__ == "__main__":
    from sys import argv
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    result = cur.fetchall()
    for row in result:
        print("{}".format(row))
    cur.close()
    db.close()
