#!/usr/bin/python3

import unittest
import uuid
import datetime
from models.base_model import BaseModel
from models import storage


class TestBase(unittest.TestCase):

    def test_initialization_no_kwargs(self):
        base = BaseModel()
        self.assertIsInstance(uuid.UUID(base.id), uuid.UUID)
        self.assertIsInstance(base.created_at, datetime.datetime)
        self.assertIsInstance(base.updated_at, datetime.datetime)

    def test_initialise_with_kwargs(self):
        kwargs = {
            'id': str(uuid.uuid4()),
            'created_at': '2022-02-15T12:34:56.789012',
            'updated_at': '2022-02-15T12:34:56.789012',
        }
        base = BaseModel(**kwargs)
        self.assertIsInstance(uuid.UUID(base.id), uuid.UUID)
        self.assertEqual(base.created_at.isoformat(), kwargs['created_at'])
        self.assertEqual(base.updated_at.isoformat(), kwargs['updated_at'])

    def test___str__(self):
        kwargs = {
            'id': str(uuid.uuid4()),
            'created_at': '2022-02-15T12:34:56.789012',
            'updated_at': '2022-02-15T12:34:56.789012',
        }
        base = BaseModel(**kwargs)
        self.assertEqual(str(base), "[BaseModel] ({}) {}".format
                         (kwargs['id'], base.__dict__))

    def test_save_method(self):
        base = BaseModel()
        original_updated_at = base.updated_at
        base.save()
        # Check if updated_at is changed after calling save
        self.assertNotEqual(base.updated_at, original_updated_at)

    def test_to_dict_method(self):
        base = BaseModel()
        base_dict = base.to_dict()
        # Check if the returned value is a dictionary
        self.assertIsInstance(base_dict, dict)
        # Check if the dictionary has the expected keys
        self.assertIn('__class__', base_dict)
        self.assertIn('id', base_dict)
        self.assertIn('created_at', base_dict)
        self.assertIn('updated_at', base_dict)

    def test_storage_interaction(self):
        base = BaseModel()
        base.save()
        # Check if the new method is called when creating a new instance
        self.assertIn(f"{base.__class__.__name__}.{base.id}", storage.all())

    def test_edge_cases(self):
        # Test edge cases
        pass
