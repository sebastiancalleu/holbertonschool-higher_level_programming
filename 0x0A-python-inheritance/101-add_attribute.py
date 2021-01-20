#!/usr/bin/python3
"""
this function adds a new attributes
and raise a error if cant add
"""


def add_attribute(obj, att, value):
    """
    add_attribute
    function that adds a new attribute

    arguments
        obj - the object
        att - the att
        value - the value
    """
    if not hasattr(obj, "__dict___"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
