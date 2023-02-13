#!/usr/bin/python3
""" function that writes an Object to a text file,
using a JSON representation """
import json


def save_to_json_file(my_obj, filename):
    """ opening a file in write mode and use the dumps()
    to convert it into a string """
    with open(filename, 'w', encoding='utf-8') as f:
        return json.dump(my_obj, f)
