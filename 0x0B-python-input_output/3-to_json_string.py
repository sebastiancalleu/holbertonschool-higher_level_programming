#!/usr/bin/python3
"""
function to convert to json
"""
import json


def to_json_string(my_obj):
    """
    to_json_string
    function to convert to json

    arguments
        my_obj - object to convert
    """
    return json.dumps(my_obj)
