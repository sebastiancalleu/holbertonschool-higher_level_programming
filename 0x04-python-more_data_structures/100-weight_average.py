#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return (0)
    prod = 0
    sum = 0
    for i in range(0, len(my_list)):
        prod += my_list[i][0] * my_list[i][1]
        sum += my_list[i][1]
    return (prod / sum)
