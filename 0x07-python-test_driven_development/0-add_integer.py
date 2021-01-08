#!/usr/bin/python3
"""
function that adds 2 integers or floats.
a is the first number.
b is the second number.
"""


def add_integer(a, b=98):
    """
    add two integers or floats and return the result.
    """
    if not (isinstance(a, int)) and not (isinstance(a, float)):
        raise TypeError("a must be an integer")
    elif not (isinstance(b, int)) and not (isinstance(b, float)):
        raise TypeError("b must be an integer")
    else:
        if isinstance(a, float):
            a = int(a)
        if isinstance(b, float):
            b = int(b)
        return (a + b)
