#!/usr/bin/python3
"""In this module a class LockedClass is defined"""


class LockedClass(object):
    """Class to create a new LockedCLass object"""
    def __setattr__(self, name, value):
        """Custom implementation of the __setattr__ magic method"""
        if name == "first_name":
            self.__dict__[name] = value
        else:
            n = self.__class__.__name__
            raise AttributeError(f"'{n}' object has no attribute '{name}'")
