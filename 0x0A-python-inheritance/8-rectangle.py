#!/usr/bin/python3
"""
define a basegeometry class.
"""


class BaseGeometry:
    """
    BaseGeometry Class
    """
    def area(self):
        """
        area
        public instance method to define the area of
        the geometry
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        integer_validator
        public instance method to validate value as a int.
        """
        if not type(value) is int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greate than 0".format(name))


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
