#!/usr/bin/python3
"""Creating a Class named square thats defines square
   With private instance size
   and Error checks
"""


class Square:
    """Private instance size"""
    size = None

    def size(self):
        self.size

    def size(self, value):
        self.size = value

    def __init__(self, size=0):
        self.size = size
    """Defining area"""
    def area(self):
        """checking for TypeError
        """
        if type(self.size) is not int:
            raise TypeError('size must be an integer')
        """Checking for ValueError
        """
        if self.size < 0:
            raise ValueError('size must be >= 0')
        """Returning Area
        """
        return self.size * self.size
