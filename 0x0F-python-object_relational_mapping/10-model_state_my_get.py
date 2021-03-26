#!/usr/bin/python3
'''
Select data from states table and return the first row
the print the state id of that first element
the element to search is given by the user.
'''

import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    state = (session.query(State).order_by(State.id).filter
             (State.name == sys.argv[4]).first())
    if state:
        print(state.id)
    else:
        print("Not found")
    session.close()
