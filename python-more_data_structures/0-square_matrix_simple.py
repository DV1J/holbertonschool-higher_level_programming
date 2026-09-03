#!/usr/bin/python3
def square(a):
    return a * a


def square_matrix_simple(matrix=[]):
    new_matrix = []
    for num in range(len(matrix)):
        for num1 in range(len(matrix[num])):
            sq = map(square, (matrix[num1]))
            new_matrix.append(list(sq))
        return (new_matrix)
