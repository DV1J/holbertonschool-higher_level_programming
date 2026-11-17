#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return list()
    pascal = []
    for num in range(n):
        row = [1] * (num + 1)
        for i in range(1, num):
            row[i] = pascal[num - 1][i - 1] + pascal[num - 1][i]
        pascal.append(row)
    return pascal
