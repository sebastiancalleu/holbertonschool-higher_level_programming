#!/usr/bin/python3
"""
function to read a file
"""


def read_file(filename=""):
    """
    read_file
    function to read a file

    arguments
        filename - the file
    """
    with open(filename, mode="r", encoding="UTF8") as textfile:
        print(textfile.read(), end="")
