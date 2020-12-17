#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newmatrix = [row[:] for row in matrix]
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            newmatrix[i][j] = matrix[i][j] ** 2
    return (newmatrix)
