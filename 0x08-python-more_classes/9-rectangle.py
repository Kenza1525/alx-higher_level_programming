#!/usr/bin/python3

""" class Rectangle that defines a rectangle """


class Rectangle:
    """ Content of the class """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """ evaluates the area and return it """
        return self.width * self.height

    def perimeter(self):
        """" returns the perimeter """
        if self.width == 0 or self.height == 0:
            return 0
        return ((self.width + self.height) * 2)

    def __str__(self):
        """ prints the rectangle using the character # """
        if self.width == 0 or self.height == 0:
            return ""
        shape = ""
        for i in range(self.height):
            for j in range(self.width):
                shape += str(self.print_symbol)
            if i != self.height - 1:
                shape += "\n"
        return shape

    def __repr__(self):
        """ returns string representattion of rectangle """
        return f'Rectangle({self.width}, {self.height})'

    def __del__(self):
        """ Deleting an instance """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ returns the area of the biggest rectangle """
        if isinstance(rect_1, Rectangle) is not True:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if isinstance(rect_2, Rectangle) is not True:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if Rectangle.area(rect_1) < Rectangle.area(rect_2):
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """ returns a new Rectangle instance """
        return cls(size, size)
