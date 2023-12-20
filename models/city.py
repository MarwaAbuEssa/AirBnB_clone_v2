#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship


class City(BaseModel):
    """ The city class, contains state ID and name
        Inherits from SQLAlchemy links to cities.

    Attributes:
        __tablename__ (str): name of MySQL table to store Cities.
        name (sqlalchemy String): City name.
        state_id (sqlalchemy String): state id.
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    places = relationship("Place", backref="cities", cascade="delete")
