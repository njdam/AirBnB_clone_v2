#!/usr/bin/python3
"""A file that bears a class DBStorage to manage database storage
for hbnb clone
"""

from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place, place_amenity
from models.amenity import Amenity
from models.review import Review

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import urllib.parse
from os import getenv


class DBStorage:
    """DBStorage class to manage storage hbnb clone models in SQL database.
    """
    __engine = None
    __session = None

    def __init__(self):
        """In DBStorage class to initialise SQL database storage"""
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV')

        DATABASE_URL = "mysql+mysqldb://{}:{}@{}:3306/db".format(
                user, pwd, host, db
                )
        self.__engine = create_engine(DATABASE_URL, pool_pre_ping=True)

        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """A function that return dictionary format of current models."""
        obj_dict = dict()
        classes = (User, State, City, Amenity, Place, Review)
        if cls is None:
            for class_t in classes:
                query = self.__session.query(class_t)
                for obj in query.all():
                    obj_key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                    obj_dict[obj_key] = obj
        else:
            query = self.__session.query(cls)
            for obj in query.all():
                obj_key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                obj_dict[obj_key] = obj

        return (obj_dict)

    def new(self, obj):
        """A function that add an object to the current database."""
        if obj is not None:
            try:
                self.__session.add(obj)
                self.__session.flush()
                self.__session.refresh(obj)
            except Exception as e:
                self.__session.rollback()
                raise e

    def save(self):
        """A function that commit all changes to database."""
        self.__session.commit()

    def delete(self, obj=None):
        """A function to delete current database session obj if not None."""
        if obj is not None:
            obj_query = self.__session.query(type(obj))
            obj_filter = obj_query.filter(type(obj).id == obj.id)
            obj_filtered.delete(synchronize_session=False)

    def reload(self):
        """A function that loads storage database."""
        Base.metadata.create_all(self.__engine)
        SessionFactory = sessionmaker(
                bind=self.__engine, expire_on_commit=False
                )
        self.__session = scoped_session(SessionFactory)()

    def close(self):
        """A function that closes storage engine."""
        self.__session.close()
