#!/usr/bin/python3
"""Script to retrieve from a database"""
from sys import argv
import MySQLdb

conn_params = {
    'user': argv[1],
    'passwd': argv[2],
    'db': argv[3],
}


def main():
    """Entry point"""
    conn = MySQLdb.connect(**conn_params)
    cursor = conn.cursor()
    query = "SELECT * FROM states ORDER BY states.id"
    cursor.execute(query)
    for i in list(cursor):
        print(i)
    conn.close()


if __name__ == '__main__':
    main()
