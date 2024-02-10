#!/usr/bin/python3
"""Define City"""
from models.base_model import BaseModel


class City(BaseModel):
    """A City with state_id and name also empty string"""

    name = ""
    state_id = ""
