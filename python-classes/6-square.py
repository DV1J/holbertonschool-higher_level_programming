#!/usr/bin/python3
"""Creating a Class named square thats defines square
   With private instance size
   and Error checks
"""


class Square:
    """A class that defines Square by its size
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple and value < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    """Defining area"""
    def area(self):
        """Returning Area
        """
        return self.__size * self.__size

    def my_print(self):
        if self.size == 0:
            print()
        for i in range(self.size):
            print('#' * self.size)
