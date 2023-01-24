#!/usr/bin/python3

"""  class Square that defines a square """


class Square:
    """ Content of the class """

    def __init__(self, size=0):
        """ Attribute Method """

        self.__size = size

        if isinstance(size, int) is not True:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """" return the area of the square """
        return (int(self.__size) ** 2)
