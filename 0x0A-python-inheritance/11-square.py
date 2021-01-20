#!/usr/bin/python3
"""
define a basegeometry class.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square
    class that inherits from Rectangle class
    this class define a square.
    """
    def __init__(self, size):
        """
        constructor

        size = the size of the square.
        height = the height of the rectangle.
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        area
        public instance method to calculate
        the area of the square
        """
        return self.__size ** 2

    def __str__(self):
        """
        __str__
        string documentation of the class square
        """
        return("[{}] {}/{}".format("Square", self.__size, self.__size))
