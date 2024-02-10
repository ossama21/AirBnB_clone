#!/usr/bin/python3
from models.base_model import BaseModel
import sys
import os

# Add the project directory to the Python path
current_directory = os.path.dirname(os.path.abspath(__file__))
project_directory = os.path.join(current_directory, "..")
# Adjust the path accordingly
sys.path.append(project_directory)


"""
Contains the module user
"""


class User(BaseModel):
    """The user Model"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
