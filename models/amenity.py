#!/usr/bin/python3
""" A file that bear State class Module for HBNB project """

from models.base_model import BaseModel, Base

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class Amenity(BaseModel, Base):
    """ A class Amenity for representing amenities data set models """
    __tablename__ = 'amenities'

    name = Column(
            String(128), nullable=False
            ) if getenv('HBNB_TYPE_STORAGE') == 'db' else ''
