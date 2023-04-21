#!/usr/bin/python3
"""
Script lists all State objects from hbtn_0e_6_usa
"""


from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

db_user = argv[1]
db_pass = argv[2]
db_name = argv[3]

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(db_user,
                           db_pass, db_name))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    for row in session.query(State).all():
        print("{}: {}".format(row.id, row.name))
