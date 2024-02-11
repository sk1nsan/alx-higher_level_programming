#!/usr/bin/python3
""" Rectangle class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Square init function"""
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string representation of square"""
        return "[Square] ({}) {}/{}"\
            " - " "{}".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update values of square"""
        attributes = ["id", "size", "x", "y"]
        if len(args) > 0:
            for attr, value in zip(attributes, args):
                setattr(self, attr, value)
        else:
            for key in kwargs.keys():
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        attrs = ["id", "size", "x", "y"]
        return {k: getattr(self, k) for k in attrs}
