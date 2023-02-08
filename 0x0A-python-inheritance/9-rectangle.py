#!/usr/bin/python3
""" Class Rectangle that inherits from BaseGeometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Gives the name of the class and calculates its area """
    def __init__(self, width, height):
        """ Initialize attributes width and height """
        self.__width = width
        BaseGeometry.integer_validator(self, "width", self.__width)
        self.__height = height
        BaseGeometry.integer_validator(self, "height", self.__height)

    def area(self):
        """ Calculates the area of the Rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ String representation of the class name """
        return f"[{Rectangle.__name__}] {self.__width}/{self.__height}"
