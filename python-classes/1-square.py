#!/usr/bin/python3
"""Creating a Class named square thats defines square
   With private instance size
"""


class Square:
    """private instance __size"""
    __size = None
    """Defining size"""
    def __init__(self, size):
        self.__size = size
