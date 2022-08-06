#!/usr/bin/python3
"""Script to retrieve from a database"""


def main():
    """Entry point"""
    from sys import argv
    import MySQLdb

    conn_params = {
        'user': argv[1],
        'passwd': argv[2],
        'db': argv[3],
    }

    conn = MySQLdb.connect(**conn_params)
    cursor = conn.cursor()
    query = "SELECT * FROM states WHERE name=%s ORDER BY states.id"
    cursor.execute(query, (argv[4],))
    for i in list(cursor):
        print(i)
    conn.close()


if __name__ == '__main__':
    main()
