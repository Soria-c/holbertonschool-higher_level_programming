#!/usr/bin/python3
"""Script that lists all City objects from a given database"""


if __name__ == '__main__':
    from relationship_city import City, Base
    from relationship_state import State
    from sqlalchemy import (create_engine)
    from sqlalchemy.engine.url import URL
    from sys import argv
    from sqlalchemy.orm import sessionmaker

    conn_params = {
        'drivername': 'mysql+mysqldb',
        'username': argv[1],
        'password': argv[2],
        'host': 'localhost',
        'database': argv[3]
    }

    engine = create_engine(URL.create(**conn_params), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    with Session() as session:
        re = session.query(City, State).filter_by(state_id=State.id)\
            .order_by(City.id).all()
        for i, j in re:
            print(f"""{i.id}: {i.name} -> {j.name}""")
