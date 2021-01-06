#!/usr/bin/python3
" A class Square that defines a square "


class Square:
    """ Square class
    """
    def __init__(self, size=0, position=(0, 0)):
        """[Constructor]
        Keyword Arguments:
            size {int} -- [description] (default: {0})
            position {tuple} -- [the first argument is the name of the
            spaces to the left, the second argument is the new lines
            before print] (default: {(0, 0)})
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """[obtain the data]
        Returns:
            [int] -- [size]
        """
        return self.__size

    @size.setter
    def size(self, value):
        """[]
        Arguments:
            value {[int]} -- [size]
        Raises:
            TypeError: [size must be an integer]
            ValueError: [size must be >= 0]
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """[summary]
        Returns:
            [tuple] -- [description]
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ position setter
        """
        if ((isinstance(value, tuple)) and len(value) == 2 and
                (value[0] >= 0 and value[1] >= 0) and
                (isinstance(value[0], int)) and (isinstance(value[1], int))):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """
        Public instance method that returns the current square area
        Returns: Area of the aquare
        """
        return self.__size ** 2

    def my_print(self):
        """
        Public instance method that prints in the square with the character #
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print((" " * self.__position[0]) + ("#" * self.__size))