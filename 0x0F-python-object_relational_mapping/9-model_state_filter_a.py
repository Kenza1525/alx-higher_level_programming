#!/usr/bin/python3
""" lists all State objects that contain the letter a """

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == '__main__':
    user = argv[1]
    passwd = argv[2]
    db = argv[3]

    engine = create_engine(f'mysql+mysqldb://{user}:\
            {passwd}@localhost:3306/{db}')
    Base.metadata.create_all(engine)

    session = sessionmaker(bind=engine)()

    state_with_a = session.query(State)\
                          .filter(State.name.like('%a%'))\
                          .order_by(State.id).all()

    for row in state_with_a:
        print(f'{row.id}: {row.name}')
    session.close()
