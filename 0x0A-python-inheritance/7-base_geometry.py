#!/usr/bin/python3
"""In this module the class BaseGeometry is defined"""


class BaseGeometry:
    """Class to create a new BaseGeometry object"""
    def area(self):
        """Raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Checks for errors and raises exceptions"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
