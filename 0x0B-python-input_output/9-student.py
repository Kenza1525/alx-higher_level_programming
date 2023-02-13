#!/usr/bin/python3
""" class Student that defines a student """


class Student:
    """ The class defines a student's first and last name
    and his age """

    def __init__(self, first_name, last_name, age):
        """ Initializes first_name, last_name and age attributes """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ retrieves a dictionary representation of a
        Student instance """
        return self.__dict__
