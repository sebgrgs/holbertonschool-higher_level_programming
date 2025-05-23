#!/usr/bin/python3
"""
Module that prints all City objects from the database hbtn_0e_14_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(City, State).filter(City.state_id == State.id).all()

    for city, state in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
