#!/usr/bin/python3
'''
Select cities names from states joined from cities
and filter it for the state name that the user enter
then print it in comma separated format.
'''
import sys
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT cities.name FROM cities\
        JOIN states ON cities.state_id = states.id\
            WHERE states.name = %s ORDER BY cities.id ASC", (sys.argv[4], ))
    query_rows = cur.fetchall()
    if len(query_rows) == 0:
        print()
    else:
        for i in range(len(query_rows)):
            if i + 1 == len(query_rows):
                print(query_rows[i][0])
            else:
                print(query_rows[i][0] + ', ', end="")
    cur.close()
    conn.close()
