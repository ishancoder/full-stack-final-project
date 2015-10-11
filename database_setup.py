import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base;
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()
########################################################

#setup your database here!!!!

############INSERT AT THE END OF THE FILE#####################################
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.create_all(engine)
