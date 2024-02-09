import unittest
from unittest.mock import patch
from io import StringIO
import uuid
from console import HBNBCommand

class TestHBNBCommand(unittest.TestCase):

    
    def test_do_help_all(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help all")
        self.assertEqual(f.getvalue().strip(), 'Prints all string representation of instances based on the class name.')
    
    def test_do_all(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
        self.assertIn('[',f.getvalue().strip())
        self.assertIn(']',f.getvalue().strip())

    # Test Cases for user class with normal commands
    def test_do_create_User(self):
        # run create command with no class name
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
        self.assertEqual(f.getvalue().strip(), "** class name missing **")

        # run create command with no unexistent class name
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create user")
        self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
        self.assertIsInstance(uuid.UUID(f.getvalue().strip()), uuid.UUID)

    def test_do_all_Users(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all user")
        self.assertEqual('** class doesn\'t exist **',f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all User")
        self.assertIn('[User]',f.getvalue().strip())

    def test_do_show_User(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
        self.assertEqual('** class name missing **',f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show user")
        self.assertEqual('** class doesn\'t exist **',f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User ")
        self.assertEqual('** instance id missing **',f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User a5c038a9-00cc-41d1-9a11-f59333d0f0e")
        self.assertEqual('** no instance found **',f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            uid = f.getvalue().strip()
            HBNBCommand().onecmd("show User {}".format(uid))
        expected = "[User] ({})".format(uid, uid)   
        self.assertIn(expected, f.getvalue().strip())
    
    def test_do_destroy_User(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
        self.assertEqual('** class name missing **',f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy user")
        self.assertEqual('** class doesn\'t exist **',f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User ")
        self.assertEqual('** instance id missing **',f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User a5c038a9-00cc-41d1-9a11-f59333d0f0e")
        self.assertEqual('** no instance found **',f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            uid = f.getvalue().strip()
            HBNBCommand().onecmd("destroy User {}".format(uid))
        expected = "[User] ({})".format(uid, uid)   
        self.assertNotIn(expected, f.getvalue().strip())
    
    def test_do_update_User(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
        self.assertEqual('** class name missing **',f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update user")
        self.assertEqual('** class doesn\'t exist **',f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User ")
        self.assertEqual('** instance id missing **',f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User a5c038a9-00cc-41d1-9a11-f59333d0f0e")
        self.assertEqual('** no instance found **',f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            uid = f.getvalue().strip()
            HBNBCommand().onecmd("update User {} email \"aibnb@mail.com\"".format(uid))
            HBNBCommand().onecmd("show User {}".format(uid))
        expected = "'email': 'aibnb@mail.com'"   
        self.assertIn(expected, f.getvalue().strip())
    
    # Test cases for User with precmd
 
    def test_precmd_create_User(self):
        # run create command with no class name
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(".create")
        self.assertEqual(f.getvalue().strip(), "*** Unknown syntax: .create")

        # run create command with no unexistent class name
        #with patch('sys.stdout', new=StringIO()) as f:
        #    HBNBCommand().onecmd("user.create")
        #self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.create")
        self.assertIsInstance(uuid.UUID(f.getvalue().strip()), uuid.UUID)

    def test_precmd_all_Users(self):
        #with patch('sys.stdout', new=StringIO()) as f:
        #    HBNBCommand().onecmd("user.all ")
        #self.assertEqual('** class doesn\'t exist **',f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.all")
        self.assertIn('[User]',f.getvalue().strip())

    def test_precmd_show_User(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(".show")
        self.assertEqual('*** Unknown syntax: .show',f.getvalue().strip())

        #with patch('sys.stdout', new=StringIO()) as f:
        #    HBNBCommand().onecmd("user.show")
        #self.assertEqual('** class doesn\'t exist **',f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.show")
        self.assertEqual('** instance id missing **',f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.show (a5c038a9-00cc-41d1-9a11-f59333d0f0e)")
        self.assertEqual('** no instance found **',f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.create")
            uid = f.getvalue().strip()
            HBNBCommand().onecmd("User.show({})".format(uid))
        expected = "[User] ({})".format(uid, uid)   
        self.assertIn(expected, f.getvalue().strip())
    
    def test_precmd_destroy_User(self):
        #with patch('sys.stdout', new=StringIO()) as f:
        #    HBNBCommand().onecmd(".destroy")
        #self.assertEqual('*** Unknown syntax: .destroy',f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("user.destroy")
        self.assertEqual('** class doesn\'t exist **',f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.destroy")
        self.assertEqual('** instance id missing **',f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.destroy(a5c038a9-00cc-41d1-9a11-f59333d0f0e)")
        self.assertEqual('** no instance found **',f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.create")
            uid = f.getvalue().strip()
            HBNBCommand().onecmd("User.destroy({})".format(uid))
        expected = "[User] ({})".format(uid, uid)   
        self.assertNotIn(expected, f.getvalue().strip())
    
    def test_precmd_update_User(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(".update")
        self.assertEqual('*** Unknown syntax: .update',f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("user.update")
        self.assertEqual('** class doesn\'t exist **',f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.update")
        self.assertEqual('** instance id missing **',f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.update(a5c038a9-00cc-41d1-9a11-f59333d0f0e)")
        self.assertEqual('** no instance found **',f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            uid = f.getvalue().strip()
            HBNBCommand().onecmd("User.update({}, email, \"aibnb@mail.com\")".format(uid))
            HBNBCommand().onecmd("User.show({})".format(uid))
        expected = "'email': 'aibnb@mail.com'"   
        self.assertIn(expected, f.getvalue().strip())
    








    # Test Cases for BaseModel class with normal commands
    def test_do_create_BaseModel(self):
        # run create command with no class name
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
        self.assertEqual(f.getvalue().strip(), "** class name missing **")

        # run create command with no unexistent class name
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create base_model")
        self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
        self.assertIsInstance(uuid.UUID(f.getvalue().strip()), uuid.UUID)

    def test_do_all_BaseModel(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all base_model")
        self.assertEqual('** class doesn\'t exist **',f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all BaseModel")
        self.assertIn('[BaseModel]',f.getvalue().strip())

    def test_do_show_BaseModel(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
        self.assertEqual('** class name missing **',f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show base_model")
        self.assertEqual('** class doesn\'t exist **',f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel ")
        self.assertEqual('** instance id missing **',f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel a5c038a9-00cc-41d1-9a11-f59333d0f0e")
        self.assertEqual('** no instance found **',f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            uid = f.getvalue().strip()
            HBNBCommand().onecmd("show BaseModel {}".format(uid))
        expected = "[BaseModel] ({})".format(uid, uid)   
        self.assertIn(expected, f.getvalue().strip())
    
    def test_do_destroy_BaseModel(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
        self.assertEqual('** class name missing **',f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy base_model")
        self.assertEqual('** class doesn\'t exist **',f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel ")
        self.assertEqual('** instance id missing **',f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel a5c038a9-00cc-41d1-9a11-f59333d0f0e")
        self.assertEqual('** no instance found **',f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            uid = f.getvalue().strip()
            HBNBCommand().onecmd("destroy BaseModel {}".format(uid))
        expected = "[BaseModel] ({})".format(uid, uid)   
        self.assertNotIn(expected, f.getvalue().strip())
    
    def test_do_update_BaseModel(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
        self.assertEqual('** class name missing **',f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update base_model")
        self.assertEqual('** class doesn\'t exist **',f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel ")
        self.assertEqual('** instance id missing **',f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel a5c038a9-00cc-41d1-9a11-f59333d0f0e")
        self.assertEqual('** no instance found **',f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            uid = f.getvalue().strip()
            HBNBCommand().onecmd("update BaseModel {} email \"aibnb@mail.com\"".format(uid))
            HBNBCommand().onecmd("show BaseModel {}".format(uid))
        expected = "'email': 'aibnb@mail.com'"   
        self.assertIn(expected, f.getvalue().strip())
    
    # Test cases for User with precmd
 
    def test_precmd_create_BaseModel(self):
        # run create command with no class name
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(".create")
        self.assertEqual(f.getvalue().strip(), "*** Unknown syntax: .create")

        # run create command with no unexistent class name
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("base_model.create")
        self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.create")
        self.assertIsInstance(uuid.UUID(f.getvalue().strip()), uuid.UUID)

    def test_precmd_all_BaseModel(self):
        #with patch('sys.stdout', new=StringIO()) as f:
        #    HBNBCommand().onecmd("base_model.all ")
        #self.assertEqual('** class doesn\'t exist **',f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.all")
        self.assertIn('[BaseModel]',f.getvalue().strip())

    def test_precmd_show_BaseModel(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(".show")
        self.assertEqual('*** Unknown syntax: .show',f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("base_model.show")
        self.assertEqual('** class doesn\'t exist **',f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.show")
        self.assertEqual('** instance id missing **',f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.show (a5c038a9-00cc-41d1-9a11-f59333d0f0e)")
        self.assertEqual('** no instance found **',f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.create")
            uid = f.getvalue().strip()
            HBNBCommand().onecmd("BaseModel.show({})".format(uid))
        expected = "[BaseModel] ({})".format(uid, uid)   
        self.assertIn(expected, f.getvalue().strip())
    
    def test_precmd_destroy_BaseModel(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(".destroy")
        self.assertEqual('*** Unknown syntax: .destroy',f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("base_model.destroy")
        self.assertEqual('** class doesn\'t exist **',f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.destroy")
        self.assertEqual('** instance id missing **',f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.destroy(a5c038a9-00cc-41d1-9a11-f59333d0f0e)")
        self.assertEqual('** no instance found **',f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.create")
            uid = f.getvalue().strip()
            HBNBCommand().onecmd("BaseModel.destroy({})".format(uid))
        expected = "[BaseModel] ({})".format(uid, uid)   
        self.assertNotIn(expected, f.getvalue().strip())
    
    def test_precmd_update_BaseModel(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(".update")
        self.assertEqual('*** Unknown syntax: .update',f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("base_model.update")
        self.assertEqual('** class doesn\'t exist **',f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.update")
        self.assertEqual('** instance id missing **',f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.update(a5c038a9-00cc-41d1-9a11-f59333d0f0e)")
        self.assertEqual('** no instance found **',f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            uid = f.getvalue().strip()
            HBNBCommand().onecmd("BaseModel.update({}, email, \"aibnb@mail.com\")".format(uid))
            HBNBCommand().onecmd("BaseModel.show({})".format(uid))
        expected = "'email': 'aibnb@mail.com'"   
        self.assertIn(expected, f.getvalue().strip())


if __name__ == '__main__':
    unittest.main()
