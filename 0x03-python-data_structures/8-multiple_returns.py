#!/usr/bin/python3
def multiple_returns(sentence):
    if (len(sentence) == 0):
        newtuple = (len(sentence), None)
    else:
        newtuple = ((len(sentence)), sentence[0])
    return(newtuple[0], newtuple[1])
