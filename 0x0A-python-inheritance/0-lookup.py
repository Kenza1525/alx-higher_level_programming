#!/usr/bin/python3
""" returns the list of available attributes and methods of an object """


def lookup(obj):
    """ Return the list of objects """
    return list(dir(obj))
