#!/usr/bin/python3
"""Script that deletes all State objects
with a name containing the letter 'a' from a given database"""

if __name__ == '__main__':
    from sys import argv
    from model_state import Base, State
    from sqlalchemy import (create_engine)
    from sqlalchemy.engine.url import URL
    from sqlalchemy.orm import sessionmaker

    conn_params = {
        'drivername': 'mysql+mysqldb',
        'username': argv[1],
        'password': argv[2],
        'host': 'localhost',
        'database': argv[3]
    }

    engine = create_engine(URL.create(**conn_params), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    with Session() as session:
        session.query(State).filter(State.name.like('%a%'))\
            .delete(synchronize_session=False)
        session.commit()
