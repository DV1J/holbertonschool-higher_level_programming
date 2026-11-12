#!/bin/usr/python3
import json
""" A function that returns an object (Python data structure)
    represented by a JSON string
"""


def from_json_string(my_str):
    """Returns object represented by json string"""
    return json.loads(my_str)
