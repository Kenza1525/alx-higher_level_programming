#!/usr/bin/python3
""" Class Square that defines a square """


class Square:
    """ Defines attributes, get the area and prints the square """

    def __init__(self, size=0):
        """ Initialize theinstance attribute """
        self.size = size

    @property
    def size(self):
        """ Gets the value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """ Sets the value of size """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Returns the area of the square"""
        return self.__size ** 2

    def __eq__(self, other):
        """ Magic method for equality """
        return self.size == other.size

    def __ne__(self, other):
        """ Magic method for inequality """
        return self.size != other.size

    def __lt__(self, other):
        """"Magic method for < """
        return self.size < other.size

    def __le__(self, other):
        """ Magic method for <= """
        return self.size <= other.size

    def __gt__(self, other):
        """ Magic Method for > """
        return self.size > other.size

    def __ge__(self, other):
        """ Magic method for >= """
        return self.size >= other.size
