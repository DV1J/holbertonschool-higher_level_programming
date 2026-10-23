#!/usr/bin/python3
"""A function that returns True if the object is
an instance of a class that inherited (directly or indirectly)
"""


def inherits_from(obj, a_class):
    """checking if obj is an instance of a class
    """
    if isinstance(type(obj), a_class) or type(obj) is not a_class:
        return True
    else:
        return False
