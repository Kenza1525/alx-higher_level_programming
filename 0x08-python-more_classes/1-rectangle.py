#!/usr/bin/python3

""" class Rectangle that defines a rectangle """


class Rectangle:
    """ Content of the class """

    def __init__(self, width=0, height=0):
        """ Initialize attribute instance """
        self.width = width
        self.height = height

    @property
    def width(self):
        """" width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if isinstance(value, int) is not True:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """" height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if isinstance(value, int) is not True:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
