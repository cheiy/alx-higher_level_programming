#!/usr/bin/python3
"""
Safe from SQL injection
Script takes in an argument, sanitizes it and then displays all values in the
states table of hbtn_0e_0_usa where name matches the argument
"""
if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                         database=argv[3])
    search = argv[4]
    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name = %(name)s  ORDER BY
            id ASC""", {'name': search})
    res = cur.fetchall()
    for row in res:
        print("{}".format(row))
    cur.close()
    db.close()
