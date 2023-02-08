#!/usr/bin/python3
""" class Square that inherits from Rectangle """
Rectangle = __import__("9-rectangle").Rectangle
BaseGeometry = __import__("8-rectangle").BaseGeometry


class Square(Rectangle):
    """ set the size value and calculate the Square area """

    def __init__(self, size):
        """ Initialize the size attribute """
        self.__size = size
        BaseGeometry.integer_validator(self, "size", self.__size)

    def area(self):
        """ Calculates and returns area """
        return self.__size ** 2

    def __str__(self):
        """ Prints the name of the class in string format """
        name = self.__class__.__base__.__name__
        return f"[{name}] {self.__size}/{self.__size}"
