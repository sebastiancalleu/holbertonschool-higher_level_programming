#!/usr/bin/python3
"""
class to define a square
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square
    class to define a square
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        str
        public instance method
        string representation of class
        """
        return "[Square] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)