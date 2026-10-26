#!/usr/bin/python3
"""Class Square that inherits Rectangle from (9-rectangle.py)"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """size"""
    def __init__(self, size):
        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size

    """changing the str return"""
    def __str__(self):
        return (f'[Square] {self.__size}/{self.__size}')
