#!/usr/bin/python3
"""
function to write in a file
"""


def write_file(filename="", text=""):
    """
    write_file
    function to write in a file

    arguments
        filename - the file
        text - text to write
    """
    with open(filename, mode="w+", encoding="UTF8") as textfile:
        return textfile.write(text)
