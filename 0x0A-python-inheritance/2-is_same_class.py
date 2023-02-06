#!/usr/bin/python3
""" eturns True if the object is exactly an instance of the specified class """


def is_same_class(obj, a_class):
    """ Check if an object is an instance of a class """
        return type(obj) is a_class
