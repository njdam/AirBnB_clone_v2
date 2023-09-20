#!/usr/bin/python3
"""Unittest for console.py"""
import unittest
import pep8
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO


class TestHBNBCommand(unittest.TestCase):
    
    