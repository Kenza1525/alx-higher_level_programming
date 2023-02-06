#!/usr/bin/python3
"""Returns True or False based on if
the object is an instance of a class"""


def inherits_from(obj, a_class):
    """Return True or False"""
    return isinstance(obj, a_class) and type(obj) != a_class
