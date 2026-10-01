#!/usr/bin/python3
"""Creating a Class named square thats defines square
   With private instance size
   and Error checks
"""


class Square:
    """private instance __size"""
    __size = None
    """Defining size"""
    def __init__(self, size=0):
        """cheking fore TypeError"""
        if type(size) is not int:
            raise TypeError('size must be an integer')
        """Checking for ValueError"""
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
