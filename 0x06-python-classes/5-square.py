#!/usr/bin/python3

""" class Square that defines a square """


class Square:
    """ Content of the class """
    def __init__(self, size=0):
        """ Attribute Method that initialize object attribute """
        self.__size = size

    @property
    def size(self):
        """ Retrieves size """
        return self.__size

    @size.setter
    def size(self, value):
        """ Allows modification of size """
        self.__size = value

        if isinstance(self.__size, int) is not True:
            raise TypeError("size must be an integer")

        if self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """" Returns the area of the square """
        return (int(self.__size) ** 2)

    def my_print(self):
        """ Prints in stdout the square with the character # """
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
        if self.__size == 0:
            print()
