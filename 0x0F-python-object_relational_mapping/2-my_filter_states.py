#!/usr/bin/python3
"""
Script takes in an argument and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument
"""
if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                         database=argv[3])
    search = argv[4]
    cur = db.cursor()
    query = """SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY
            id ASC""".format(search)
    cur.execute(query)
    res = cur.fetchall()
    for row in res:
        print("{}".format(row))
    cur.close()
    db.close()
