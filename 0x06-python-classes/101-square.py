#!/usr/bin/python3
""" Class Square that defines a square """


class Square:
    """ Defines attributes, get the area and prints the square """

    def __init__(self, size=0, position=(0, 0)):
        """ Initialize theinstance attributes """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ Gets the value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """ Sets the value of size """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ Gets the position """
        return self.__position

    @position.setter
    def position(self, value):
        """ Sets the position of value """
        if type(value) != tuple or type(value[0]) != int or\
                type(value[1]) != int or len(value) != 2 or value[0] < 0\
                or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        """ Returns the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """ Prints the square """
        if self.size == 0:
            print("")

        for i in range(self.position[1]):
            print("")
        for square in range(self.size):
            print(" " * self.position[0], end="")
            print("#", end="")
            #if i != self.size - 1:
                #print('\n')

    def __str__(self):
        """ Prints the string representation of the square """
        string = ""
        if self.size == 0:
            return string
        for i in range(self.position[1]):
            string += "\n"
        for square in range(self.size):
            string += " " * self.position[0] + "#" * self.size + '\n'
        return string
