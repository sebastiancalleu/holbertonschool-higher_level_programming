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
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
