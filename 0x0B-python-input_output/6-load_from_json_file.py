#!/usr/bin/python3
"""
function to load json from a file
"""
import json


def load_from_json_file(filename):
    """
    load_from_json_file
    function to load json from a file

    arguments
        filename - the file
    """
    with open(filename, mode="r", encoding="UTF8") as textfile:
        return json.load(textfile)
