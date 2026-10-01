#!/usr/bin/python3
"""A function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """Added TypeError message here as pycodestyle says its too long
    """
    msg = ('matrix must be a matrix (list of lists) of integers/floats')
    """Checking if Matrix is not a list or  if matrix is empty
       Then raises a TypeError if it is
    """
    if type(matrix) is not list or matrix == []:
        raise TypeError(msg)
    """Chcking if div is a number by checking its type
       Raises a typeError if it is
    """
    if type(div) is not (int, float):
        raise TypeError('div must be a number')
    """Checking if div is zero
       if it is then raise zeroDivisionError
    """
    if div == 0:
        raise ZeroDivisionError('division by zero')
    new_matrix = []
    for i in matrix:
        if type(i) is not list or i == []:
            raise TypeError(msg)
        new_new_matrix = []
        for j in i:
            num = round(j / div, 2)
            new_new_matrix.append(num)
        new_matrix.append(new_new_matrix)
    return (new_matrix)
