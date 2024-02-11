#!/usr/bin/python3
import unittest
import datetime
from models.amenity import Amenity
from models import storage
from models.base_model import BaseModel

"""tests tests"""

class TestAmenity(unittest.TestCase):
    """Test for Amenity class"""
    def test_initialization_no_kwargs(self):
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertEqual(amenity.name, "")

        amenity = Amenity(name="Amenity")
        self.assertEqual(amenity.name, "Amenity")

    def test_attribute_value(self):
        amenity = Amenity()

        amenity.name = "New name"
        self.assertEqual(amenity.name, "New name")

    def test_string_representation(self):
        # Test the __str__ method
        amenity = Amenity()
        expected_str = "[Amenity] ({}) {}".format(amenity.id, amenity.__dict__)
        self.assertEqual(str(amenity), expected_str)

    def test_save_method(self):
        # Test the save method
        amenity = Amenity()
        original_updated_at = amenity.updated_at
        amenity.save()
        self.assertNotEqual(amenity.updated_at, original_updated_at)

    def test_to_dict_method(self):
        # Test the to_dict method
        amenity = Amenity()
        amenity.name = "New Amen"
        amenity_dict = amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertIn('__class__', amenity_dict)
        self.assertIn('id', amenity_dict)
        self.assertIn('created_at', amenity_dict)
        self.assertIn('updated_at', amenity_dict)
        self.assertEqual(amenity_dict['name'], "New Amen")

    def test_storage_interaction(self):
        # Test interaction with storage
        amenity = Amenity()
        amenity.save()
        self.assertIn(
            f"{amenity.__class__.__name__}.{amenity.id}", storage.all())

    def test_inheritance(self):
        # Test inheritance from BaseModel
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertIsInstance(amenity, BaseModel)

if __name__ == "__main__":
    unittest.main()
