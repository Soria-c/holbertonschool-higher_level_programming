import json
import csv
import turtle

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
    
    @classmethod
    def save_to_file_csv(cls, list_objs):
        c = cls.__name__
        l = [i.to_dictionary().values() for i in list_objs]
        with open(f"{c}.csv", mode="w", encoding="utf-8") as file:
            csv.writer(file).writerows(l)

    @classmethod
    def load_from_file_csv(cls):
        c = cls.__name__
        l = []
        bp = []
        with open(f"{c}.csv", mode="r", encoding="utf-8") as file:
            input = csv.reader(file)
            for i in input:
                l.append(i)
        if (c == "Rectangle"):
            bp = ["id", "width", "height", "x", "y"]
        elif (c == "Square"):
            bp = ["id", "size", "x", "y"]
        length = len(bp)
        instances = []
        for j in l:    
            dct = {bp[i]: int(j[i]) for i in range(length)}
            instances.append(cls.create(**dct))
        return instances
    
    @staticmethod
    def draw(list_rectangles, list_squares):
        
        draw = turtle.Turtle()
        for i in list_rectangles:
            draw.goto(i.x, i.y)
            draw.pendown()
            for j in range(2):
                draw.forward(i.width)
                draw.right(90)
                draw.forward(i.height)
                draw.right(90)
            draw.penup()    
        for k in list_squares:
            draw.goto(k.x, k.y)
            draw.pendown()
            for v in range(2):
                draw.forward(k.width)
                draw.right(90)
                draw.forward(k.height)
                draw.right(90)
            draw.penup()
        turtle.done()
        


    
