#!/usr/bin/python3
"""
Module prints state with the name passed in argument
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    db_user = argv[1]
    db_pass = argv[2]
    db = argv[3]
    state = argv[4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(db_user,
                           db_pass, db))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    res = session.query(State).filter(State.name == func.binary(state))
    if len(res.all()) == 0:
        print("Not found")
    else:
        for row in res:
            print("{}".format(row.id))
