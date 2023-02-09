#!/usr/bin/python3
""" class MagicClass """
from math import pi


class MagicClass:
    """ Initializes attributes, calculates area and circumference """
    def __init__(self, radius=0):
        """ Initialize radius attribute """
        if type(radius) not in (int, float):
            raise TypeError("radius must be a number")
        self.radius = radius

    def area(self):
        """ Calculates the area """
        return pi * (self.radius ** 2)

    def circumference(self):
        """ Calculates the circumference """
        return 2 * pi * self.radius
