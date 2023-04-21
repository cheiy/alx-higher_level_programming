#!/usr/bin/python3
"""
Module fetches cities by state
"""
from sys import argv
from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    db_user = argv[1]
    db_pass = argv[2]
    db = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(db_user,
                           db_pass, db))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(State, City).filter(State.id == City.state_id)
    for city in cities.all():
        print("{}: ({}) {}".format(record.State.name, record.City.id,
                                   record.City.name))
