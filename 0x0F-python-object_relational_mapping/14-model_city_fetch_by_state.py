#!/usr/bin/python3
'''
this script make a join of states from cities
'''


import sys
from model_state import Base, State
from model_city import Base, City

from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    for city in session.query(City).order_by(City.id).join(State):
        print("{}: ({}) {}".format(city.states.name, city.id, city.name))
    session.close()
