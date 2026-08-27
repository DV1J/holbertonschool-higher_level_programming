#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j in i:
            if j != '':
                print("{:d}".format(j),end=' ')
            if j % 3 == 0:
                print('')
            