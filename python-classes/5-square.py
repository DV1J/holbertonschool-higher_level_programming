#!/usr/bin/python3
"""Creating a Class named square thats defines square
   With private instance size
   and Error checks
"""


class Square:
    """A class that defines Square by its size
    """
    def __init__(self, size=0):
        """Size = Size of the square"""
        self.size = size

    @property
    def size(self):
        """Gets the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """checking for TypeError
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        """Checking for ValueError
        """
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def my_print(self):
        if self.size == 0:
            print()
        for i in range(self.size):
            print('#' * self.size)

    """Defining area"""
    def area(self):
        """Returning Area
        """
        return self.__size * self.__size
