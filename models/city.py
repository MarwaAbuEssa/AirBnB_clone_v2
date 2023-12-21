#!/usr/bin/python3
"""Defines the City class."""
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ a city for a MySQL DB.

    Inherits from SQLAlchemy Base , links to cities table.

    Attributes:
        __tablename__ (str): Cities table name.
        name (sqlalchemy String): City name.
        state_id (sqlalchemy String): state id of City.
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    places = relationship("Place", backref="cities", cascade="delete")
