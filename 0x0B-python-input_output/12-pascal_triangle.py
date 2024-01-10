#!/usr/bin/python3
""" This is module 12-pascal_triangle.py """


def pascal_triangle(n):
    """ This defines the calculation of pascals triangel """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    pascal = [[1]]
    for row in range(1, n):
        p_row = pascal[-1]
        n_row = []

        for i in range(1, len(p_row)):
            n_row.append(p_row[i - 1] + p_row[i])

        n_row = [1] + n_row + [1]
        pascal.append(n_row)
    return pascal
