#!/usr/bin/python3

""" class Square that defines a square """


class Square:
    """ Content of the class """

    def __init__(self, size=0, position=(0, 0)):
        """ Attribute method that initializes objet attributes """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """ Retrieve the position """
        return self.__position

    @position.setter
    def position(self, value):
        """ Allows Modification of position """
        self.__position = value

        if type(value) != tuple or len(value) != 2 or type(value[0]) != int \
                or type(value[1]) != int or value[0] < 0 or value[1] < 0:
                    raise TypeError("position must be \
                            a tuple of 2 positive integers")

    def area(self):
        """" Returns the area of the square """
        return (int(self.__size) ** 2)

    def my_print(self):
        """" prints in stdout the square with the character # """
        if self.size == 0:
            print("")
        else:
            for i in range(self.position[1]):
                print("")
            for row in range(self.size):
                print(" " * self.position[0], end="")
                for col in range(self.size):
                    print("#", end="")
                print("")
