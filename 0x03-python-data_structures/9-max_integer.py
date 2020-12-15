#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return (None)
    else:
        max = -1000000000
        for i in range(0, len(my_list)):
            if (my_list[i] > max):
                max = my_list[i]
        return(max)
