#!/usr/bin/python3
"""
This script lists all states with a name starting with N
from the database hbtn_0e_0_usa
"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                         database=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    res = cur.fetchall()
    for row in res:
        print("{}".format(row))
    cur.close()
    db.close()
