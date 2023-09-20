#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""

from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage

from os import getenv

storage = DBStorage() if os.getenv(
    'HBNB_TYPE_STORAGE') == 'db' else FileStorage()
"""
storage = DBStorage() if getenv(
        'HBNB_TYPE_STORAGE'
        ) == 'db' else FileStorage()
"""
# This is Unique for FileStorage or DBStorage in their all instance models
storage.reload()
