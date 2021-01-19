#!/usr/bin/python3
"""
function to determine if a object
is a exactly instance of a class
"""


def is_same_class(obj, a_class):
    """
    is_same_class
    function to determine if a object
    is a exactly instance of a class

    arguments
        obj - the object
        a_class - the class
    """
    if type(obj) == a_class:
        return True
    return False
