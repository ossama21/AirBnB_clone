#!/usr/bin/python3
import unittest
import datetime
from models.city import City
from models import storage
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    def test_initialization_no_kwargs(self):
        city = City()
        self.assertIsInstance(city, City)
        self.assertEqual(city.name, "")

        city = City()
        city.name = "Amenity"
        self.assertEqual(city.name, "Amenity")

    def test_attribute_value(self):
        city = City()

        city.name = "New name"
        self.assertEqual(city.name, "New name")

    def test_string_representation(self):
        # Test the __str__ method
        city = City()
        city.name = "New Amen"
        expected_str = "[City] ({}) {}".format(city.id, city.__dict__)
        self.assertEqual(str(city), expected_str)

    def test_save_method(self):
        # Test the save method
        city = City()
        original_updated_at = city.updated_at
        city.save()
        self.assertNotEqual(city.updated_at, original_updated_at)

    def test_to_dict_method(self):
        # Test the to_dict method
        city = City()
        city.name = "New Amen"
        city_dict = city.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertIn('__class__', city_dict)
        self.assertIn('id', city_dict)
        self.assertIn('created_at', city_dict)
        self.assertIn('updated_at', city_dict)
        self.assertEqual(city_dict['name'], "New Amen")

    def test_storage_interaction(self):
        # Test interaction with storage
        city = City()
        city.name = "New Amen"
        city.save()
        self.assertIn(f"{city.__class__.__name__}.{city.id}", storage.all())

    def test_inheritance(self):
        # Test inheritance from BaseModel
        city = City()
        self.assertIsInstance(city, City)
        self.assertIsInstance(city, BaseModel)

if __name__ == "__main__":
    unittest.main()
