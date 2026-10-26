#!/usr/bin/python3
"""Class Square that inherits Rectangle from (9-rectangle.py)"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """size"""
    def __init__(self, size):
        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size
