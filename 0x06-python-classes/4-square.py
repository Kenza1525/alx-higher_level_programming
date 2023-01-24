#!/usr/bin/python3

""" class Square that defines a square """


class Square:
    """ Content of the class """

    def __init__(self, size=0):
        """ Attribute method that initialize attribute objects """

        self.__size = size

    @property
    def size(self):
        """ Retrieve the size """
        return self.__size

    @size.setter
    def size(self, value):
        """ Allows Modification of size """
        self.__size = value

        if isinstance(self.__size, int) is not True:
            raise TypeError("size must be an integer")

        if self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """" Returns the area of the square """
        return (int(self.__size) ** 2)
