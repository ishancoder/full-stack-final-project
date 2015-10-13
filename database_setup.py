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


class Puppy(Base):
	__tablename__ = 'puppy'
	id = Column(
			Integer,
			primary_key = True
		)

	name = Column(
			String(10),
			nullable = False
		)

	weight = Column(
			Double,
			nullable = False
		)

	age = Column(
			Integer,
			nullable = False
		)

	breed = Column(
			String(15),
			nullable = False
		)

	gender = Column(
			String(7),
			nullable = False
		)

	shelter_id = Column(
			Integer,
			ForeignKey('shelter.id')
		)

	shelter = relationship(Shelter)

############INSERT AT THE END OF THE FILE#####################################
engine = create_engine('sqlite:///puppyshelter.db')
Base.metadata.create_all(engine)
