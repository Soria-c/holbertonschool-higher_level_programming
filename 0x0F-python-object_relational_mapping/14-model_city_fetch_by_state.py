#!/usr/bin/python3
"""Script that that prints all City objects from a given database"""

if __name__ == '__main__':
    from model_city import City, Base
    from model_state import State
    from sqlalchemy import (create_engine)
    from sqlalchemy.engine.url import URL
    from sqlalchemy.orm import sessionmaker
    from sys import argv

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
        re = session.query(City, State).filter_by(state_id=State.id)\
            .order_by(City.id).all()
        for i, j in re:
            print(f"{j.name}: ({i.id}) {i.name}")
