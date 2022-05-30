#!/usr/bin/python3
"""In this module the class MyList is defined"""


class MyList(list):
    """Class MyList that inherits from the list object"""
    def print_sorted(self):
        """Instance method that prints a sorted list"""
        print(sorted(self))
