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
            %s ORDER BY states.id ASC"
    arg_name = f"%{argv[4]}%"
    cursor.execute(query, (arg_name,))

    rows = cursor.fetchall()
    for row in rows:
        if row[1] == argv[4]:
            print(row)
    cursor.close()
    db.close()
