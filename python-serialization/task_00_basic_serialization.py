#!/usr/bin/python3
"""Create a basic serialization module that adds the functionality to serialize
   A python dictionary to a JSON file and
   deserialize the JSON file to recreate the Python Dictionary.
"""


import pickle


def serialize_and_save_to_file(data, filename):
    """function for saving and serialize to specified file"""
    with open(filename, 'wb') as f:
        pickle.dump(data, f)


def load_and_deserialize(filename):
    """function to load and deserialize data from specified file"""
    with open(filename, 'rb') as f:
        return pickle.load(f)
