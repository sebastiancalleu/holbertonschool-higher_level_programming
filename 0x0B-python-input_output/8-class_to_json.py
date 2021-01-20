#!/usr/bin/python3
"""
function to obtain dict rep of a class
"""


def class_to_json(obj):
    """
    class_to_json
    function to obtain dict rep of a class

    arguments
        obj - the object
    """
    return obj.__dict__
