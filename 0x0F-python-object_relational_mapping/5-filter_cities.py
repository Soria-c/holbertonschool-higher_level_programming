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
    query = """SELECT cities.name FROM states
    INNER JOIN cities
    ON states.id=cities.state_id
    WHERE states.name=%s
    ORDER BY cities.id
    """
    cursor.execute(query, (argv[4],))
    print(", ".join(i[0] for i in list(cursor)))
    conn.close()


if __name__ == '__main__':
    main()
