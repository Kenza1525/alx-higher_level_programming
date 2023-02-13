#!/usr/bin/python3
""" returns the dictionary description """


def class_to_json(obj):
    """ Function that returns object attributes as a dictionnary """
    return obj.__dict__
