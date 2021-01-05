#!/usr/bin/python3
"""class to define a square"""


class Square:
    """
    square class to define a square
    attributes:
            size: private instance attribute (int).
    """
    def __init__(self, size=0):
        if not type(size) is int:
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    """
    public instance method that calculates the area of a square
    """
    def area(self):
        return self.__size * self.__size
