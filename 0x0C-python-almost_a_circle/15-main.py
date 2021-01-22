#!/usr/bin/python3
""" 15-main """
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":

    r1 = Rectangle(5, 5, 5, 5)
    r2 = Rectangle(2, 4)
    l1 = []
    Rectangle.save_to_file(l1)
    s1 = Square(3)
    s2 = Square(5)
    Square.save_to_file([s1, s2])

    with open("Rectangle.json", "r") as file:
        print(file.read())
