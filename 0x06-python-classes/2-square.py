#!/usr/bin/python3

"""" class Square that defines a square """


class Square:
    """" Content of thr class """

    def __init__(self, size=0):
        """ Atribute method that initialize oject attributes """

        self.__size = size

        if isinstance(size, int) is not True:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
