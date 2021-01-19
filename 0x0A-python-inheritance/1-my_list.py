#!/usr/bin/python3
"""
function to print a sorted list
"""


class MyList(list):
    """
    MyList
    function to print a sorted list

    arguments
        list - the list
    """
    def print_sorted(self):
        print(sorted(self))
