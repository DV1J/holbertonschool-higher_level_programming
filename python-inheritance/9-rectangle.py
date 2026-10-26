#!/usr/bin/python3
"""Write a class Rectangle that inherits from BaseGeometry
   importing BaseGeometry from 7-base_gemoetry.py
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Instantiation with width and height"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        """having integer_validator check width and height"""
        self.integer_validator('width', self.__width)
        self.integer_validator('height', self.__height)

    def area(self):
        self.area = self.__width * self.__height
        return self.area

    def __str__(self):
        return (f'[Rectangle] {self.__width}/{self.__height}')
