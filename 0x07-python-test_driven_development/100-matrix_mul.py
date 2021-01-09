#!/usr/bin/python3
"""
module to multiply matrices
"""


def matrix_mul(m_a, m_b):
    """
    matrix_mul - this function multiply matrices

    arguments
        m_a: first matrix
        m_b: second matrix

    return
    the result matrix
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    for i in m_a:
        if not isinstance(i, list):
            raise TypeError("m_a must be a list of lists")
        elif len(i) == 0:
            raise ValueError("m_a can't be empty")
        for j in i:
            if not isinstance(j, int) and not isinstance(j, float):
                raise TypeError("m_a should contain only integers or floats")
        if len(m_a[0]) != len(i):
            raise TypeError("each row of m_a must be of the same size")
    for i in m_b:
        if not isinstance(i, list):
            raise TypeError("m_b must be a list of lists")
        elif len(i) == 0:
            raise ValueError("m_b can't be empty")
        for j in i:
            if not isinstance(j, int) and not isinstance(j, float):
                raise TypeError("m_b should contain only integers or floats")
        if len(m_b[0]) != len(i):
            raise TypeError("each row of m_b must be of the same size")
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    prodmatrix = [[0 for i in range(len(m_b[0]))] for i in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                prodmatrix[i][j] += m_a[i][k] * m_b[k][j]
    return(prodmatrix)
