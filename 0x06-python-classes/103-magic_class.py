#!/usr/bin/python3
from math import pi

"""class MagicClass"""


class MagicClass:
    """class MagicClass"""

    def __init__(self, radius=0):
        self.radius = 0
        if type(radius) is not int:
            if type(radius) is not float:
                raise TypeError("radius must be a number")
        self.radius = radius

    def area(self):
        return self.radius**2 * pi

    def circumference(self):
        return 2 * pi * self.radius
