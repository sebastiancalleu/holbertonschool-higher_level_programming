#!/usr/bin/python3
"""
define a basegeometry class.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class to define a rectangle
    """

    def __init__(self, width, height):
        """
        constructor

        width = the width of the rectangle.
        height = the height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        area
        public instance method to calculate
        the area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        __str__
        string documentation of the class rectangle
        """
        return("[{}] {}/{}".format("Rectangle", self.__width, self.__height))
