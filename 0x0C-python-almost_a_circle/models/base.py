import json
from venv import create


class Base:
    __nb_objects = 0
    def __init__(self, id=None):
        if id:
            self.id = id
            return
        Base.__nb_objects += 1
        self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        return "[]"
    
    @classmethod
    def save_to_file(cls, list_objs):
        c = cls.__name__
        ls = []
        for i in list_objs:
            ls.append(i.to_dictionary())
        jsn = Base.to_json_string(ls)
        with open(f"{c}.json", mode="w", encoding="utf-8") as file:
            file.write(jsn)
    
    @staticmethod
    def from_json_string(json_string):
        if (json_string):
            return json.loads(json_string)
        return []
    
    @classmethod
    def create(cls, **dictionary):
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
        c = cls.__name__
        input = None
        with open(f"{c}.json", mode='r', encoding="utf-8") as file:
            input = file.read()
        ls_dct = Base.from_json_string(input)
        return [cls.create(**i) for i in ls_dct]
    
