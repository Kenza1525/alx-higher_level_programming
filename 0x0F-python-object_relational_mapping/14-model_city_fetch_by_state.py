#!/usr/bin/python3
"""  prints all City objects from the database hbtn_0e_14_usa """

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
from sys import argv

if __name__ == '__main__':
    user = argv[1]
    passwd = argv[2]
    db = argv[3]

    engine = create_engine(f'mysql+mysqldb://{user}:\
            {passwd}@localhost:3306/{db}')

    Base.metadata.create_all(engine)

    session = sessionmaker(bind=engine)()

    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        print(f'{city.state.name}: ({city.id}) {city.name}')

    session.close()
