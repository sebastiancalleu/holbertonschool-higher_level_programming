#!/usr/bin/python3
"""
function that multiplies matrices
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    lazy_matrix_mul - function to multiply
    matrices

    arguments
        m_a: first matrix
        m_b: second matrix
    """
    return(numpy.matmul(m_a, m_b))
