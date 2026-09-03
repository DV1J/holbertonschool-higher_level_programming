#!/usr/bin/python3
def square(a):
    return a * a


def square_matrix_simple(matrix=[]):
    new_matrix = []
    for num in range(len(matrix)):
        sq = map(square, (matrix[num]))
        new_matrix.append(list(sq))
    return (new_matrix)
