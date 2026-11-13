#!/usr/bin/python3
"""A function that writes an Object to a text file
   using json representation
"""
import json, sys


def save_to_json_file(my_obj, filename):
    """opeing file in write mode using with"""
    filename = 'add_item.json'
    with open(filename, 'w') as f:
        """dumping/writing data into json file"""
        my_obj = sys.argv[1:]
        return json.dump(my_obj, f)

filename = 'add_item.json'
list = []
save_to_json_file(list, filename)

def load_from_json_file(filename):
    """using with to open file in read mode"""
    filename = 'add_item.json'
    with open(filename, 'r') as f:
        """createing obj by loading contain of file into obj"""
        Obj = json.load(f)
        return Obj

filename = 'add_item.json'
list = load_from_json_file(filename)
print(list)