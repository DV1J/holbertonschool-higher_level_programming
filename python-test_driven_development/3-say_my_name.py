#!/usr/bin/python3
"""
A funtion to print first_name and last names
"""


def say_my_name(first_name, last_name=""):
    """Checking if names are string.
    if not then call TypeError
    """
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')
    print('My name is {} {}'.format(first_name, last_name))
