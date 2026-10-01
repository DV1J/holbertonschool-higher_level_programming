def matrix_divided(matrix, div):
    msg = ('matrix must be a matrix (list of lists) of integers/floats')
    if type(matrix) is not list or matrix == []:
        raise TypeError(msg)
    if type(div) is not int:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    new_matrix = []
    for i in matrix:
        new_new_matrix = []
        for j in i:
            num = round(j / div, 2)
            new_new_matrix.append(num)
        new_matrix.append(new_new_matrix)
    return (new_matrix)
