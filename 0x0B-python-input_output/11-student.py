#!/usr/bin/python3
""" class Student that defines a student """


class Student:
    """ Defines the names and age of a student """

    def __init__(self, first_name, last_name, age):
        """ Initializes the instance attributes """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Return attributes in a dictionnary format """
        attr_dict = self.__dict__
        new_dict = {}

        if type(attrs) == list:
            for key in attr_dict:
                if key in attrs:
                    new_dict[key] = attr_dict[key]
            return new_dict
        return attr_dict

    def reload_from_json(self, json):
        """ deserialize the content of json and use it as new
        instance attributes """
        for key in json:
            setattr(self, key, json[key])
