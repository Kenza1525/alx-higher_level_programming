#!/usr/bin/python3
""" class Student that defines a student """


class Student:
    """ Defines a student's first and last
    name and age """

    def __init__(self, first_name, last_name, age):
        """ Initializes the names and age attributes """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation
        of a Student instance """
        new_dict = {}
        attr_dict = self.__dict__

        if type(attrs) == list:
            for key in attr_dict:
                if key in attrs:
                    new_dict[key] = attr_dict[key]
            return new_dict
        return attr_dict
