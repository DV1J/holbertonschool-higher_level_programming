#!/usr/bin/python3
"""A function that returns True
if an object is an instance of,
or if the object is an instance of a class
"""


def is_kind_of_class(obj, a_class):
    """checking id obj is an instance of class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
