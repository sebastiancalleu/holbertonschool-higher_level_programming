#!/usr/bin/python3
"""
class to define a int with
some weird behaviors
"""


class MyInt(int):
    """
    MyInt
    class to define a int with
    some weird behaviors
    """

    def __init__(self, a):
        """
        constructor
            a - the int
        """
        self.a = a

    def __eq__(self, other):
        """
        modifying equality behavior
        """
        return self.a != other

    def __ne__(self, other):
        """
        modifying inequality behavior
        """
        return self.a == other
