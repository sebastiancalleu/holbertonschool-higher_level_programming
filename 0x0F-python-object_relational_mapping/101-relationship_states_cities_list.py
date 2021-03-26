#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from relationship_city import Base, City
from relationship_state import Base, State
from sqlalchemy.orm import Session

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
        for cities in state.cities:
            print("    {}: {}".format(cities.id, cities.name))
    session.close()
