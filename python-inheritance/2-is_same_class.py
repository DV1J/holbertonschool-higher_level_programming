#!/usr/bin/python3
"""A function that returns True
if an Object is the instance of a class
Otherwise False
"""


def is_same_class(obj, a_class):
    """Checking if obj is an instance of class
    """
    if dir(obj) == dir(a_class):
        return True
    else:
        return False
