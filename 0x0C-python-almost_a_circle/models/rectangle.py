from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        Rectangle.error_check(**{
            "width": width,
            "height": height,
            "x": x,
            "y": y
            })
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def area(self):
        return self.__width * self.__height

    def display(self):
        for i in range(self.__y):
            print()
        h = self.__height
        w = self.__width
        print("\n".join([" " * self.__x+"#" * w for i in range(h)]))

    def update(self, *args, **kwargs):
        cl = self.__class__.__name__
        r, s, i, z = ["_Rectangle__", "_Square__", "id", "size"]
        if not args:
            u = {(r + k if k != i and z else k): v for k, v in kwargs.items()}
            if cl == "Square":
                u = {(s + k if k == z else k): v for k, v in u.items()}
            if ("size" in kwargs):
                u["_Rectangle__width"] = kwargs["size"]
                u["_Rectangle__height"] = kwargs["size"]
            self.__dict__.update(u)
            return
        d = list(self.__dict__.keys())
        u, j, k = [{}, 0, 0]
        while j < len(args):
            if (k == 1 and cl == "Square"):
                u[d[k]] = args[j]
                u[d[k + 1]] = args[j]
                k += 2
                j += 1
                continue
            u[d[k]] = args[j]
            k += 1
            j += 1
        self.__dict__.update(u)

    def to_dictionary(self):
        c = self.__class__.__name__
        s = self.__dict__.items()
        dct = {(k[12:] if "Rectangle" in k else k): v for k, v in s}
        if (c == "Square"):
            ls = ["height", "width"]
            s2 = dct.items()
            dct = {(k[9:] if c in k else k): v for k, v in s2 if k not in ls}
        return dct

    def __str__(self):
        cl = self.__class__.__name__
        msg = f"[{cl}] ({self.id}) {self.__x}/{self.__y} - {self.__width}"
        if (cl == "Square"):
            return msg
        return msg + f"/{self.__height}"

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        Rectangle.error_check(**{"width": value})
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        Rectangle.error_check(**{"height": value})
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        Rectangle.error_check(**{"x": value})
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        Rectangle.error_check(**{"y": value})
        self.__y = value

    @classmethod
    def error_check(cls, **values):
        for k, v in values.items():
            if type(v) is not int:
                raise TypeError(f"{k} must be an integer")
            if v <= 0 and k in ["height", "width"]:
                raise ValueError(f"{k} must be > 0")
            if v < 0:
                raise ValueError(f"{k} must be >= 0")
