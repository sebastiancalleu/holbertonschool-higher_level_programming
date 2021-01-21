#!/usr/bin/python3
"""
class to define a base
"""


class Base:
    """
    Base
    clase to define a base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        constructor

        arguments
            id - the id
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
