#!/usr/bin/python3
""" List states from hbtn_0e_0_usa where name matches a CLI argument """

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
    query = "SELECT * FROM states WHERE name LIKE\
            '%{}%' ORDER BY states.id ASC"
    cursor.execute(query.format(argv[4]))

    rows = cursor.fetchall()
    for row in rows:
        if row[1] == argv[4]:
            print(row)
    cursor.close()
    db.close()

