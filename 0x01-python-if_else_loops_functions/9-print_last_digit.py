#!/usr/bin/env python3
def print_last_digit(number):
    if number < 0:
        i = number % -10
        i = -i
    else:
        i = number % 10
    print("{:d}".format(i), end='')
    return(i)
