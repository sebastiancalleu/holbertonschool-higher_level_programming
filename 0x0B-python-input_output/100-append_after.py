#!/usr/bin/python3
"""
function to write after a def string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    append_after
    function to write after a def string

    arguments
        filename - the file
        search_string - string to search
        new_string - string to add after match
    """
    with open(filename, mode="r+", encoding="UTF8") as sourcefile:
        lines = sourcefile.readlines()
        with open(filename, mode="w", encoding="UTF8") as textfile:
            for i in range(len(lines)):
                if search_string in lines[i]:
                    lines[i] = lines[i] + new_string
                    textfile.write(lines[i])
                else:
                    textfile.write(lines[i])
