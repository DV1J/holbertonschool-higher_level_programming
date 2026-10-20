#!/usr/bin/python3
"""Empty class Rectangle"""


class Rectangle:
    """defines Rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """Checking for TypeError"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        """Checking if width is less than 0"""
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """Checking for TypeError"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        """Checking for if height is less than 0"""
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        """printing symbol"""
        self.print_symbol
        """counting instance"""
        Rectangle.number_of_instances += 1

    def area(self):
        """Returning area"""
        return self.__height * self.__width

    def perimeter(self):
        """Checking if height or width is 0
            If it is then return perimeter 0
        """
        if self.__width == 0:
            return ('0')
        if self.__height == 0:
            return ('0')
        """Returning Perimeter"""
        return 2 * (self.__height + self.__width)

    def __str__(self):
        if self.__height == 0:
            return ('')
        if self.__width == 0:
            return ('')
        w = self.__width
        h = self.__height
        return ((str(self.print_symbol) * w + '\n') * h)[:-1]

    def __repr__(self):
        return ('Rectangle({}, {})'.format(self.width, self.height))

    def __del__(self):
        """counting if instance is decreasing"""
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Checking is rect_1 and rect_2 is and instace of Rectangle"""
        if type(rect_1) is not Rectangle:
            raise TypeError('rect_1 must be an instance of Rectangle')
        elif type(rect_2) is not Rectangle:
            raise TypeError('rect_2 must be an instance of Rectangle')
        """Checking if rect_1 is greater than rect_2"""
        if rect_1.area() > rect_2.area():
            return rect_1
        """Checking is rect_2 and rect_1 are the same values"""
        if rect_2.area() == rect_1.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
