#!/usr/bin/python3
"""
Module inserts state named Louisiana to the db
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine, func
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
    session.add(State(name="Louisiana"))
    session.commit()
    res = session.query(State).filter(State.name == func.binary("Louisiana"))\
        .first()
    print("{}".format(res.id))
