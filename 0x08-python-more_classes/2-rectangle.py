#!/usr/bin/python3
"""
class to define a Rectangle
"""


class Rectangle:
    """
    class that define a rectangle
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def height(self):
        """
        height getter

        return
          height = the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        heigh setter

        arguments
          value = the height to set.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """
        width getter

        return
          width = the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        width setter

        arguments
          value = the width to set.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """
        area - instance method that find
        the area of the rectangle

        return
          the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        perimeter - instance method that find
        the perimeter of the rectangle

        return
          the perimeter of the rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)
