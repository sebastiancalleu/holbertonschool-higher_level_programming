#!/usr/bin/python3
"""
Function that divide all elements of a matrix and return new matrix
"""


def matrix_divided(matrix, div):
    """
    matrix_divided - function that divide a matrix

    Arguments
        matrix - matrix of int or floats
        div - int of float that will divide the matrix

    Return
        newmatrix - the result of the division
    """
    newmatrix = [[] for i in range(len(matrix))]
    for i in matrix:
        for j in i:
            if not isinstance(j, int) and not isinstance(j, float):
                raise TypeError("matrix must be a matrix(list of lists)"
                                " of integers/floats")
    for i in range(1, len(matrix)):
        if len(matrix[i]) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            newmatrix[i].append(round(matrix[i][j] / div, 2))
    return (newmatrix)
