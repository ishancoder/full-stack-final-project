import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base;
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()
########################################################

#setup your database here!!!!
class Shelter(Base):
	__tablename__ = 'shelter'
	id  = Column(
			Integer,
			primary_key = True
		)

	name = Column(
			String(80),
			nullable = False
		)

	address = Column(
			String(400),
			nullable = False
		)

	phone = Column(
			String(15),
			nullable = False
		)

	email = Column(
			String(50),
			nullable = False
		)

	owner = Column(
			String(80),
			nullable = False
		)

############INSERT AT THE END OF THE FILE#####################################
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.create_all(engine)
