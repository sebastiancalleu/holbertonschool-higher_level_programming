#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return (None)
    keylist = list(a_dictionary.keys())
    vallist = list(a_dictionary.values())
    score = 0
    for i in range(0, len(vallist)):
        if (int(vallist[i]) > score):
            score = vallist[i]
    pos = vallist.index(score)
    return(keylist[pos])
