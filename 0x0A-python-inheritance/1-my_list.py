#!/usr/bin/python3
""" A class MyList that inherits from list """


class MyList(list):
    """ Inherits from list parent class """

    def print_sorted(self):
        """ Prints a sorted list """
        print(sorted(self))
