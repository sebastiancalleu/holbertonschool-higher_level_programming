#!/usr/bin/python3
"""
this function checks if a object is
inherited from a class
"""


def inherits_from(obj, a_class):
    """
    inherits_from
    this function checks if a object is
    inherited from a class

    arguments
        obj - the object
        a_class - the class
    """
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
