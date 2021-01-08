#!/usr/bin/python3
"""
function that say the name of a person
the arguments are the name and the last name of the person
"""


def say_my_name(first_name, last_name=""):
    """
    say_my_name function that prints a name

    arguments:
    first_name - string that contains the first name.
    last_name - string that contains the last name.

    return:
    none
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
