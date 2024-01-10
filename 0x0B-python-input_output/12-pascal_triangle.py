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
        
