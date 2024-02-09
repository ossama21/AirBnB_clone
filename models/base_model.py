#!/usr/bin/python3
"""
Contains the BaseModel module
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """BaseModel class"""

    def __init__(self, *args, **kwargs):
        """Constructor method"""

        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, value)

    def __str__(self):
        """Return the string representation of a class"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Saves a model in the storage"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the class"""
        diction = self.__dict__.copy()
        for key, value in diction.items():
            if key == 'created_at' or key == 'updated_at':
                diction[key] = value.isoformat()
        diction['__class__'] = self.__class__.__name__
        return diction

