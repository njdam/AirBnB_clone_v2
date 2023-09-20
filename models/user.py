#!/usr/bin/python3
"""This module defines a class User"""

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv

from models.base_model import BaseModel, Base


class User(BaseModel):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'

    email = Column(
            String(128), nullable=False
            ) if getenv('HBNB_TYPE_STORAGE') == 'db' else ''

    password = Column(
            String(128), nullable=False
            ) if getenv('HBNB_TYPE_STORAGE') == 'db' else ''

    first_name = Column(
            String(128), nullable=True
            ) if getenv('HBNB_TYPE_STORAGE') == 'db' else ''

    last_name = Column(
            String(128), nullable=True
            ) if getenv('HBNB_TYPE_STORAGE') == 'db' else ''

    places = relationship(
            'Place',
            cascade="all, delete, delete-orphan", backref='user',
            ) if getenv('HBNB_TYPE_STORAGE') == 'db' else None

    reviews = relationship(
            'Review',
            cascade="all, delete, delete-orphan", backref='user',
            ) if getenv('HBNB_TYPE_STORAGE') == 'db' else None
