#!/usr/bin/python3
def square(a):
    return a * a


def square_matrix_simple(matrix=[]):
    new_matrix = matrix[:]
    for num in range(len(matrix)):
        for num1 in range(len(matrix[num])):
            num1 += 1
            for num2 in range(len(matrix[num1])):
                num2 += 2
                sq1 = map(square, (new_matrix[num]))
                sq2 = map(square, (new_matrix[num1]))
                sq3 = map(square, (new_matrix[num2]))
                sq = list(sq1), list(sq2), list(sq3)
                return (list(sq))
