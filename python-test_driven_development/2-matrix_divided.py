def matrix_divided(matrix, div):
    new_matrix = []
    for i in matrix:
        for j in i:
            num = round(j / div, 2)
            if len(new_matrix) >= 3:
                new_new_matrix = []
                new_new_matrix.append(num)
                if len(new_new_matrix) == 2:
                    new_matrix.append(new_new_matrix)
            else:
                new_matrix.append(num)
    return(new_matrix)