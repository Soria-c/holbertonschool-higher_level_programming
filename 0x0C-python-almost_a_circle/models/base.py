#!/usr/bin/python3
"""
This module defines the classes:
    Base
"""

import json
import csv
import turtle
from os.path import exists


class Base:
    """Class to create a new Base object"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Implementation of the __init__ magic method"""
        if id:
            self.id = id
            return
        Base.__nb_objects += 1
        self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns a jsonified list of dictionaries"""
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """Creates or overwrites a json file based on an object's attributes"""
        c = cls.__name__
        ls = []
        with open(f"{c}.json", mode="w", encoding="utf-8") as file:
            if (not list_objs):
                file.write("[]")
                return
            for i in list_objs:
                ls.append(i.to_dictionary())
            jsn = Base.to_json_string(ls)
            file.write(jsn)

    @staticmethod
    def from_json_string(json_string):
        """Loads a json file a returns it as a python dictionary"""
        if (json_string):
            return json.loads(json_string)
        return []

    @classmethod
    def create(cls, **dictionary):
        """
        Creates a new instance of a Square or Rectangle object
        based on a dictionary
        """
        src = cls.__name__
        new = None
        if (src == "Rectangle"):
            new = cls(1, 1)
        elif (src == "Square"):
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """Returns a list of Square or Rectangle object based on a json file"""
        c = cls.__name__
        if (not exists(f"./{c}.json")):
            return []
        input = None
        with open(f"{c}.json", mode="r", encoding="utf-8") as file:
            input = file.read()
        ls_dct = Base.from_json_string(input)
        return [cls.create(**i) for i in ls_dct]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves an object's attribues as a csv file"""
        c = cls.__name__
        ls = [i.to_dictionary().values() for i in list_objs]
        with open(f"{c}.csv", mode="w", encoding="utf-8") as file:
            csv.writer(file).writerows(ls)

    @classmethod
    def load_from_file_csv(cls):
        """Returns a list of Square or Rectangle object based on a csv file"""
        c = cls.__name__
        ls = []
        bp = []
        with open(f"{c}.csv", mode="r", encoding="utf-8") as file:
            input = csv.reader(file)
            for i in input:
                ls.append(i)
        if (c == "Rectangle"):
            bp = ["id", "width", "height", "x", "y"]
        elif (c == "Square"):
            bp = ["id", "size", "x", "y"]
        length = len(bp)
        instances = []
        for j in ls:
            dct = {bp[i]: int(j[i]) for i in range(length)}
            instances.append(cls.create(**dct))
        return instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws a list of Square and/or Rectangle objects"""
        draw = turtle.Turtle()
        for j in [list_rectangles, list_squares]:
            for i in j:
                draw.goto(i.x, i.y)
                draw.pendown()
                for j in range(2):
                    draw.forward(i.width)
                    draw.right(90)
                    draw.forward(i.height)
                    draw.right(90)
                draw.penup()
        turtle.done()
