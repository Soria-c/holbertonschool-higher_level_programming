#!/usr/bin/python3
"""
In this module the class:
    Student
    is defined
"""


class Student:
    """Class to create a nre Student object"""
    def __init__(self, first_name, last_name, age):
        """Implementation of the __init__ magic method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns a dictionary for self attributes"""
        return self.__dict__
