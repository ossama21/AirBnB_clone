#!/usr/bin/python3
import unittest
import datetime
from models.state import State
from models import storage
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    def test_initialization_no_kwargs(self):
        state = State()
        self.assertIsInstance(state, State)
        self.assertEqual(state.name, "")

        state = State()
        state.name = "Amenity"
        self.assertEqual(state.name, "Amenity")

    def test_attribute_value(self):
        state = State()

        state.name = "New name"
        self.assertEqual(state.name, "New name")

    def test_string_representation(self):
        # Test the __str__ method
        state = State()
        state.name = "New Amen"
        expected_str = "[State] ({}) {}".format(state.id, state.__dict__)
        self.assertEqual(str(state), expected_str)

    def test_save_method(self):
        # Test the save method
        state = State()
        original_updated_at = state.updated_at
        state.save()
        self.assertNotEqual(state.updated_at, original_updated_at)

    def test_to_dict_method(self):
        # Test the to_dict method
        state = State()
        state.name = "New Amen"
        state_dict = state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertIn('__class__', state_dict)
        self.assertIn('id', state_dict)
        self.assertIn('created_at', state_dict)
        self.assertIn('updated_at', state_dict)
        self.assertEqual(state_dict['name'], "New Amen")

    def test_storage_interaction(self):
        # Test interaction with storage
        state = State()
        state.name = "New Amen"
        state.save()
        self.assertIn(f"{state.__class__.__name__}.{state.id}", storage.all())

    def test_inheritance(self):
        # Test inheritance from BaseModel
        state = State()
        self.assertIsInstance(state, State)
        self.assertIsInstance(state, BaseModel)
