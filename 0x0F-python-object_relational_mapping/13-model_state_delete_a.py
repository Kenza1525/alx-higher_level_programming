#!/usr/bin/python3
""" deletes all State objects with a name containing the letter a """

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    db = argv[3]

    engine = create_engine(f'mysql+mysqldb://{user}:\
            {passwd}@localhost:3306/{db}')

    Base.metadata.create_all(engine)

    session = sessionmaker(bind=engine)()

    state_delete = session.query(State)\
                          .filter(State.name.like('%a%'))\
                          .order_by(State.id).all()
    for state in state_delete:
        session.delete(state)

    session.commit()
    session.close()
