#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    valuelist = list(a_dictionary.values())
    keylist = list(a_dictionary.keys())
    for i in range(0, len(valuelist)):
        if (valuelist[i] == value):
            key = keylist[i]
            a_dictionary.pop(key)
    return (a_dictionary)
