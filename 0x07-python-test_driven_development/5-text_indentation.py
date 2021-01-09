#!/usr/bin/python3
"""
function that prints a text and 2 blank lines after
specials characters
"""


def text_indentation(text):
    """
    text_identation - function that split for special char

    arguments
        text: the text
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while(i < len(text)):
        if text[i] == '.' or text[i] == ':' or text[i] == '?':
            print(text[i])
            print()
            i += 1
            if text[i] == ' ':
                i += 1
        else:
            print(text[i], end="")
            i += 1
