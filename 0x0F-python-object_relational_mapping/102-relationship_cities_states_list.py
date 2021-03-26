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
    for cts in session.query(City).order_by(City.id):
        print("{}: {} -> {}".format(cts.id, cts.name, cts.state.name))
    session.close()
