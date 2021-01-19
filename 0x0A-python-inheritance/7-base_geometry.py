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
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greate than 0".format(name))
