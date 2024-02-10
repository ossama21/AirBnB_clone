#!/usr/bin/python3

import unittest
import datetime
from models.user import User
from models import storage
from models.base_model import BaseModel


class TestUser(unittest.TestCase):

    def test_initialization(self):
        # Test initialization with default values
        user = User()
        self.assertIsInstance(user, User)
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

        # Test initialization with specific values
        user = User()
        user.email = "test@example.com"
        user.password = "secret"
        user.last_name = "Doe"
        user.first_name = "John"
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "secret")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

    def test_attribute_values(self):
        # Test setting and updating attribute values
        user = User()

        user.email = "test@example.com"
        self.assertEqual(user.email, "test@example.com")

        user.password = "new_password"
        self.assertEqual(user.password, "new_password")

        user.first_name = "Jane"
        self.assertEqual(user.first_name, "Jane")

        user.last_name = "Smith"
        self.assertEqual(user.last_name, "Smith")

    def test_string_representation(self):
        # Test the __str__ method
        user = User()
        expected_str = "[User] ({}) {}".format(user.id, user.__dict__)
        self.assertEqual(str(user), expected_str)

    def test_save_method(self):
        # Test the save method
        user = User()
        original_updated_at = user.updated_at
        user.save()
        self.assertNotEqual(user.updated_at, original_updated_at)

    def test_to_dict_method(self):
        # Test the to_dict method
        user = User()
        user.email = "test@example.com"
        user.password = "secret"
        user.last_name = "Doe"
        user.first_name = "John"

        user_dict = user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertIn('__class__', user_dict)
        self.assertIn('id', user_dict)
        self.assertIn('created_at', user_dict)
        self.assertIn('updated_at', user_dict)
        self.assertEqual(user_dict['email'], "test@example.com")
        self.assertEqual(user_dict['password'], "secret")
        self.assertEqual(user_dict['first_name'], "John")
        self.assertEqual(user_dict['last_name'], "Doe")

    def test_storage_interaction(self):
        # Test interaction with storage
        user = User()
        user.save()
        self.assertIn("{}.{}".format(
            user.__class__.__name__, user.id), storage.all())

    def test_inheritance(self):
        # Test inheritance from BaseModel
        user = User()
        self.assertIsInstance(user, User)
        self.assertIsInstance(user, BaseModel)
