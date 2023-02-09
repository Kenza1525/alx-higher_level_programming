#!/usr/bin/python3
""" function that creates an Object from a “JSON file """
import json


def load_from_json_file(filename):
    """ Gets a json string from a file and
    convert it into an object """
    with open(filename, encoding="utf-8") as f:
        json.load(f)
