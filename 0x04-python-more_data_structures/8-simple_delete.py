#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    keys = list(a_dictionary)
    if (keys.count(key) != 0):
        a_dictionary.pop(key)
    return(a_dictionary)
