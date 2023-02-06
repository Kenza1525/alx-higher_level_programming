#!/usr/bin/python3
"""BaseGeometry class"""


class BaseGeometry:
    """Base geometry class"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value
        Args:
            name (str): string
            value (int): integer
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0") 
