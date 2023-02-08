#!/usr/bin/python3
""" class MyInt that inherits from int """


class MyInt(int):
    """ Inverts the behavior of __eq__ and __ne__ """
    def __eq__(self, other):
        """ Checks the inequality of two numbers """
        if isinstance(other, MyInt):
            return self != other
        return False

    def __ne__(self, other):
        """ Checks the equality of two numbers """
        return not self.__eq__(other)
