#!/usr/bin/python3
"""
In this module the class:
    Student
    is defined
"""


class Student:
    """Class to create a new Student object"""
    def __init__(self, first_name, last_name, age):
        """Implementation of the __init__ magic method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary for self attributes"""
        if (not attrs or [i for i in attrs if not isinstance(i, str)]):
            return self.__dict__
        return {i: j for i, j in self.__dict__.items() if i in attrs}
