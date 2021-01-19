#!/usr/bin/python3
"""
function to determine if a object
is a instance of a class or a inherited class
"""


def is_kind_of_class(obj, a_class):
    """
    is_kind_of_class
    function to determine if a object
    is a instance of a class or a inherited class

    arguments
        obj - the object
        a_class - the class
    """
    return isinstance(obj, a_class)
