#!/usr/bin/python3
"""In this module the class MyInt is defined"""


class MyInt(int):
    """Class to create a new MyInt object, inherits from int"""
    def __eq__(self, other):
        """Custom implementation of the __eq___ magic method"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Custom implementation of the __ne___ magic method"""
        return super().__eq__(other)
