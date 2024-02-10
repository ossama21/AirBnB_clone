#!/usr/bin/python3
"""Define Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """A review with attributes place user and text """

    place_id = ""
    user_id = ""
    text = ""
