#!/usr/bin/python3
"""
class to define a Rectangle
"""


class Rectangle:
    """
    class that define a rectangle
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        constructor

        arguments:
          width = width of the rectangle
          height = height of the rectangle
        """
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

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

    def __str__(self):
        """
        return
          string that prints the rectangle in # chars
        """
        string = ""
        if not isinstance(self.print_symbol, str):
            print("wtf")
            self.print_symbol = str(self.print_symbol)
        for i in range(self.__height):
            if i == (self.__height - 1):
                string += self.print_symbol * self.__width
            else:
                string += self.print_symbol * self.__width + "\n"
        return (string)

    def __repr__(self):
        """
        return
          string to implement a new instance
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        deletes the instance and print a message
        """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        bigger_or_equal
        staticmethod to chose the big rectangle

        arguments
          rect_1: first rectangle
          rect_2: second rectangle

        return
          the bigger rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
