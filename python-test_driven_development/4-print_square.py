#!/usr/bin/python3
"""A function that prints a square
"""
def print_square(size):
    """checking if size is int if not then rasie TypeError
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')
    """checking if size is not negative if it is rasie ValueError
    """
    if size < 0:
        raise ValueError('size must be >= 0')
    """Checking if size is not a float and below 0 then raise TypeError
    """
    if type(size) is float and size < 0:
        raise TypeError('size must be an integer')
    for i in range(size):
        for j in range(size):
            print('#', end=' ')
        print()
