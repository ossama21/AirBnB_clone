#!/usr/bin/python3
import unittest
import datetime
from models.place import Place
from models import storage
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    def test_initialization_no_kwargs(self):
        place = Place()
        self.assertIsInstance(place, Place)
        self.assertEqual(place.name, "")

        place = Place(name="Amenity")
        self.assertEqual(place.name, "Amenity")

    def test_attribute_value(self):
        place = Place()

        place.name = "New name"
        self.assertEqual(place.name, "New name")

    def test_string_representation(self):
        # Test the __str__ method
        place = Place()
        expected_str = "[Place] ({}) {}".format(place.id, place.__dict__)
        self.assertEqual(str(place), expected_str)

    def test_save_method(self):
        # Test the save method
        place = Place()
        original_updated_at = place.updated_at
        place.save()
        self.assertNotEqual(place.updated_at, original_updated_at)

    def test_to_dict_method(self):
        # Test the to_dict method
        place = Place()
        place.name = "New Amen"
        place_dict = place.to_dict()
        self.assertIsInstance(place_dict, dict)
        self.assertIn('__class__', place_dict)
        self.assertIn('id', place_dict)
        self.assertIn('created_at', place_dict)
        self.assertIn('updated_at', place_dict)
        self.assertEqual(place_dict['name'], "New Amen")

    def test_storage_interaction(self):
        # Test interaction with storage
        place = Place()
        place.name = "New Amen"
        place.save()
        self.assertIn(
            f"{place.__class__.__name__}.{place.id}", storage.all())

    def test_inheritance(self):
        # Test inheritance from BaseModel
        place = Place()
        self.assertIsInstance(place, Place)
        self.assertIsInstance(place, BaseModel)
