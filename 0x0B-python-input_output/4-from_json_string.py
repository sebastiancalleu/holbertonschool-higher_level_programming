#!/usr/bin/python3
"""
function to convert from json
"""
import json


def from_json_string(my_str):
    """
    from_json_string
    function to convert from json

    arguments
        my_str - the json rep
    """
    return json.loads(my_str)
