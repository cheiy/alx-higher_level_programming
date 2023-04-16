#!/usr/bin/python3
"""
script lists all cities from the db hbtn_0e_4_usa
"""
if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                         database=argv[3])
    cur = db.cursor()
    query = """SELECT c.id, c.name, s.name FROM cities AS c
            INNER JOIN states AS s ON c.state_id = s.id
            ORDER BY c.id ASC"""
    cur.execute(query)
    res = cur.fetchall()
    for row in res:
        print("{}".format(row))
    cur.close()
    db.close()
