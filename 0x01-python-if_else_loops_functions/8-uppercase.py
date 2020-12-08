#!/usr/bin/python3
def uppercase(str):
    for copy in str:
        if (ord(copy) > 96 and ord(copy) < 123):
            copy = chr(ord(copy) - 32)
        else:
            pass
        print("{}".format(copy), end='')
    print("")
