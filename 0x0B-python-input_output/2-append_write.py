#!/usr/bin/python3
"""
function to append text to a file
"""


def append_write(filename="", text=""):
    """
    append_write
    function to append text to a file

    arguments
        filename - the file
        text - the text to append
    """
    with open(filename, mode="a", encoding="UTF8") as textfile:
        return textfile.write(text)
