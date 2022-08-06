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
    query = """SELECT cities.id, cities.name, states.name
    FROM cities
    INNER JOIN states
    ON cities.state_id=states.id
    ORDER BY cities.id
    """
    cursor.execute(query)
    for i in list(cursor):
        print(i)
    conn.close()


if __name__ == '__main__':
    main()
