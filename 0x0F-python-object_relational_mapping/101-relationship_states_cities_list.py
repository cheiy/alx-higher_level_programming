#!/usr/bin/python3
"""
Prints all State objects  and corresponding City objects, contained in the
hbtn_0e_101_usa database
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    user = argv[1]
    db_pass = argv[2]
    db = argv[3]
    engine = create_engine(
                            'mysql+mysqldb://{}:{}@localhost/{}'
                            .format(user, db_pass, db),
                            pool_pre_ping=True
                                )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    res = session.query(State).all()
    for state in res:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))
    session.close()
