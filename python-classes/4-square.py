#!/usr/bin/python3
"""Creating a Class named square thats defines square
   With private instance size
   and Error checks
"""


class Square:
    size = None

    def size(self):
        self.size

    def size(self, value):
        self.size = value

    def __init__(self, size=0):
        self.size = size
    """Defining area"""
    def area(self):
        if type(self.size) is not int:
            raise TypeError('size must be an integer')
        if self.size < 0:
            raise ValueError('size must be >= 0')
        return self.size * self.size
