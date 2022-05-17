#!/usr/bin/python3
"""In this module a class MagicClass is defined"""


class MagicClass:
    """Class to create a MagicClass object"""
    def __init__(self, radius):
        """Initialize a new instance of MagicClass"""
        if (type(radius) is not int) and (type(radius) is not float):
            raise TypeError("radius must be a number")
        self._radius = radius

    def area(self):
        """Returns the area of a given MagicClass (circle) object"""
        return self._radius ** 2 * math.pi

    def circumference(self):
        """Returns the perimeter of a given MagicClass (circle) object"""
        return 2 * math.pi * self._radius
