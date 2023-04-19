#!/usr/bin/python3
"""  takes the name of a state as an argument and
     list all cities of a particular state """

import MySQLdb
from sys import argv


if __name__ == '__main__':
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3])

    cursor = db.cursor()
    query = "SELECT cities.name FROM cities\
            JOIN states ON cities.state_id = states.id\
            WHERE states.name = %s"

    state_name = argv[4]
    cursor.execute(query, (state_name,))
    rows = cursor.fetchall()
    city_name = []
    for row in rows:
        city_name.append(', '.join(row))
    print(', '.join(city_name))

    cursor.close()
    db.close()
