#!/usr/bin/python3
"""
script takes in name of a state as argument and lists all cities of that state
using the db hbtn_0e_4_usa
"""
if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                         database=argv[3])
    cur = db.cursor()
    query = """select DISTINCT city.name FROM cities AS city INNER JOIN states
    AS state ON city.state_id=state.id WHERE state.name='{}'""".format(argv[4])
    cur.execute(query)
    res = cur.fetchall()
    cities = []
    for row in res:
        cities += row
    total = len(cities)
    count = 0
    for city in cities:
        count += 1
        if count < total:
            print(city, end=", ")
        else:
            print(city)
    cur.close()
    db.close()
