#!/usr/bin/python3
"""
function to save json in file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    save_to_json_file
    function to sabe json in file

    arguments
        my_obj - the json rep
        filename - the file
    """
    with open(filename, mode="w", encoding="UTF8") as textfile:
        textfile.write(json.dumps(my_obj))
