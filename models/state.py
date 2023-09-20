#!/usr/bin/python3
""" State Module for HBNB project """

from models.base_model import BaseModel, Base
from models.city import City

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class for dealing with all instances about State models"""
    __tablename__ = 'states'
    name = Column(
            String(128), nullable=False
            ) if getenv('HBNB_TYPE_STORAGE') == 'db' else ''

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship(
                'City',
                cascade='all, delete, delete-orphan', backref='state'
                )
    else:
        @property
        def cities(self):
            """A function to return cities attr in State class."""
            from models import storage
            ret_cities = []
            for value in storage.all(City).values():
                if value.state_id == self.id:
                    ret_cities.append(value)

            return (ret_cities)
