from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Shelter

engine = create_engine('sqlite:///puppyshelter.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)
session = DBSession()

shelter1 = Shelter(name = "Rajat Patwa puppy shelter",
					address = "Street no. 7, House no. 8 ANewGalaxy, Mars.",
					phone = "a cool phone number",
					email = "a cool email address",
					owner = "Rajat Patwa")

session.add(shelter1)
session.commit()