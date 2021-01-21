#!/usr/bin/python3
"""
function to make a pascal triangle
"""


def pascal_triangle(n):
    """
    pascal_triangle
    function to make a pascal triangle

    arguments
        n - the pascal size
    """
    lsls = [[1] for i in range(n)]

    for i in range(1, n):
        for j in range(1, i + 1):
            if j == i:
                    lsls[i].append(1)
            else:
                if i < 4:
                    lsls[i].append(i)
                else:
                    lsls[i].append(lsls[i - 1][j] + lsls[i - 1][j - 1])

    return lsls
