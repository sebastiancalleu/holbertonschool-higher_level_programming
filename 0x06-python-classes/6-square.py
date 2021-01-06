#!/usr/bin/python3
"""class to define a square"""


class Square:
    """
    square class to define a square
    attributes:
            size: private instance attribute (int).
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not type(value) is int:
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not type(position) is tuple and not type(position[0]) is int and
                not type(position[1]) is int and len(position) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    """
    public instance method that calculates the area of a square
    """
    def area(self):
        return self.__size * self.__size

    """
    public instance method that print a square with "#" characters
    """
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for k in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for l in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
