#!/usr/bin/python3
""" Function that adds a new attribute to an object if it’s possible """


def add_attribute(obj, name, value):
    """ checks if the object has a __dict__ attribute, adds
    one if it is present """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
