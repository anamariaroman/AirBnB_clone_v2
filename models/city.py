#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Column, ForeignKey


class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    __table__ = "cities"
    name = Column(String(128), nullable=False, ForeignKey=('state.id'))
    state_id = Column(String(60), nullable=False, ForeignKey=('states.id'))
