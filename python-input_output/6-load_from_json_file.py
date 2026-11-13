#!/usr/bin/python3
"""A function that creates an Object from a json file"""
import json


def load_from_json_file(filename):
    """using with to open file in read mode"""
    with open(filename, 'r') as f:
        """createing obj by loading contain of file into obj"""
        Obj = json.load(f)
        return Obj
