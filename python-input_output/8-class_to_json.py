#!/usr/bin/python3
"""A function that returns the dictionary description
with simple data structure for json serialization"""


def class_to_json(obj):
    """returning obj"""
    return obj.__dict__
