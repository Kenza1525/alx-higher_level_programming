#!/usr/bin/python3
""" function that returns an object (Python data structure)
represented by a JSON string """
import json


def from_json_string(my_str):
    """ Uses the loads() function for deserialization """
    return json.loads(my_str)
