#!/usr/bin/python3
"""A class student tha defines a student"""


class Student:
    """instatiation with public attributes"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """checking if attrs is a list"""
        if type(attrs) is list:
            """making a new dictionary"""
            new_dict = {}
            for attri in attrs:
                if attri in self.__dict__:
                    new_dict[attri] = self.__dict__[attri]
            return new_dict
        return self.__dict__
