#!/usr/bin/python3
"""Creating a Class named square thats defines square
   With private instance size
"""


class Square:
    """private instance __size"""
    __size = None
    """Defining size"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size msut be >= 0')
        self.__size = size
