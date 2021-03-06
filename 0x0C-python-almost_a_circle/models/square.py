#!/usr/bin/python3
"""
This module defines the classes:
    Square
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Class to create a new Square object"""
    def __init__(self, size, x=0, y=0, id=None):
        """Implementation of the __init__ magic method"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Size setter"""
        return self.width

    @size.setter
    def size(self, value):
        """Size getter"""
        self.width = value
        self.height = value
