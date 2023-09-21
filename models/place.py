#!/usr/bin/python3
""" Place Module for HBNB project """

from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity

from sqlalchemy import Column, String, ForeignKey, Table, Float, Integer
from sqlalchemy.orm import relationship
from os import getenv


place_amenity = Table(
        'place_amenity',
        Base.metadata,
        Column(
            'place_id', String(60), ForeignKey('places.id'),
            primary_key=True, nullable=False
            ),
        Column(
            'amenity_id', String(60), ForeignKey('amenities.id'),
            primary_key=True, nullable=False
            )
        )
"""This table represents the relationship between Place and Amenity recs."""


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    city_id = Column(
            String(60), ForeignKey('cities.id'), nullable=False
            ) if getenv('HBNB_TYPE_STORAGE') == 'db' else ''

    user_id = Column(
            String(60), ForeignKey('users.id'), nullable=False
            ) if getenv('HBNB_TYPE_STORAGE') == 'db' else ''

    name = Column(
            String(128), nullable=False
            ) if getenv('HBNB_TYPE_STORAGE') == 'db' else ''

    description = Column(
            String(1024), nullable=True
            ) if getenv('HBNB_TYPE_STORAGE') == 'db' else ''

    number_rooms = Column(
            Integer, default=0, nullable=False
            ) if getenv('HBNB_TYPE_STORAGE') == 'db' else 0

    number_bathrooms = Column(
            Integer, default=0, nullable=False
            ) if getenv('HBNB_TYPE_STORAGE') == 'db' else 0

    max_guest = Column(
            Integer, default=0, nullable=False
            ) if getenv('HBNB_TYPE_STORAGE') == 'db' else 0

    price_by_night = Column(
            Integer, default=0, nullable=False
            ) if getenv('HBNB_TYPE_STORAGE') == 'db' else 0

    latitude = Column(
            Float, nullable=True
            ) if getenv('HBNB_TYPE_STORAGE') == 'db' else 0.0

    longitude = Column(
            Float, nullable=True
            ) if getenv('HBNB_TYPE_STORAGE') == 'db' else 0.0

    amenity_ids = []

    reviews = relationship(
            'Review',
            cascade="all, delete, delete-orphan", backref='place'
            ) if getenv('HBNB_TYPE_STORAGE') == 'db' else None

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        amenities = relationship(
                'Amenity',
                secondary=place_amenity, viewonly=False,
                backref='place_amenities'
                )
    else:
        @property
        def reviews(self):
            """A function that returns Review of a given place."""
            from models import storage
            results = []
            for value in storage.all(Review).values():
                if value.place_id == self.id:
                    results.append(value)

            return (results)

        @property
        def amenities(self):
            """A function to return amenities of Place models."""
            from models import storage
            results = []
            for value in storage.all(Amenity).values():
                if value.id in self.amenity_ids:
                    result.append(value)

            return (results)

        @amenities.setter
        def amenities(self, value):
            """A function that adds amenity to a place."""
            if type(value) is Amenity:
                if value.id not in self.amenity_ids:
                    self.amenity_ids.append(value.id)
