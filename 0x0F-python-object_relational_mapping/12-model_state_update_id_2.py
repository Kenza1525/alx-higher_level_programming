#!/usr/bin/python3
""" changes the name of a State object """

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == '__main__':
    user = argv[1]
    passwd = argv[2]
    db = argv[3]

    engine = create_engine(f'mysql+mysqldb://{user}:\
            {passwd}@localhost:3306/{db}')

    Base.metadata.create_all(engine)

    session = sessionmaker(bind=engine)()

    name_update = session.query(State).filter(State.id == 2).first()
    name_update.name = 'New Mexico'

    session.commit()
    session.close()
