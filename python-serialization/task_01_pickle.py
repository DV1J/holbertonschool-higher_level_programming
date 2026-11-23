#!/usr/bin/pyhton3
"""Create a custom python class named CustomObject"""


import pickle


class CustomObject:

    """Class attributes"""
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_stdent = is_student

    """method to print attributes"""
    def display(self):
        print('Name:', self.name)
        print('Age:', self.age)
        print('Is Student:', self.is_student)

    """method to serialize and save instance of object"""
    def serialize(self, filename):
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None

    """method to deserialize and load instance of object"""
    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except Exception:
            return None
