#!/usr/bin/python3
""" A File that bear class Review module for the HBNB project """

from models.base_model import BaseModel, Base

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class Review(BaseModel, Base):
    """ Review class to store review information of models """
    __tablename__ = 'reviews'

    # Storing the reviewed place_id
    place_id = Column(
            String(60), ForeignKey('places.id'), nullable=False
            ) if getenv('HBNB_TYPE_STORAGE') == 'db' else ''

    # Storing the review user_id
    user_id = Column(
            String(60), ForeignKey('users.id'), nullable=False
            ) if getenv('HBNB_TYPE_STORAGE') == 'db' else ''

    # Storing the review text
    text = Column(
            String(1024), nullable=False
            ) if getenv('HBNB_TYPE_STORAGE') == 'db' else ''
