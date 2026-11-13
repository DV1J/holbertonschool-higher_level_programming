#!/usr/bin/python3
"""A function that writes an Object to a text file
   using json representation
"""
import json


def save_to_json_file(my_obj, filename):
    """opeing file in write mode using with"""
    with open(filename, 'w') as f:
        """dumping/writing data into json file"""
        return json.dump(my_obj, f)
