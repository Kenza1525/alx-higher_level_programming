#!/usr/bin/python3
"""create a Rectangle class with widht and height attribute"""


class Rectangle:
    """Rectangle class created with width and height
    Attributes:
        number_of_instances (int): shows the number of instances created
        and deleted
        print_symbo (str): characters to print
    """
    number_of_instances = 0
    print_symbol = "#"
    """create a functions for ractengle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, height):
        """set height"""
        if type(height) != int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        """get width"""
        return self.__width

    @width.setter
    def width(self, width):
        """set width"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    def area(self):
        """return the area of a rectangle"""
        return self.height * self.width

    def perimeter(self):
        """return perimeter of a rectangle"""
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.height + self.width)

    def __str__(self):
        """print a rectangle"""
        pr = []
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.height):
            for j in range(self.width):
                pr.append(str(self.print_symbol))
            if i < self.height - 1:
                pr.append("\n")
        return "".join(pr)

    def __repr__(self):
        """return the rectangle width and height"""
        return f"Rectangle ({self.__width}, {self.__height})"

    def __del__(self):
        """delete a instance"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if Rectangle.area(rect_1) < Rectangle.area(rect_2):
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance"""

        return cls(size, size)
