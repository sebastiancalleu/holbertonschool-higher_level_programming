#!/usr/bin/python3
""" script to request a URL """

import requests
import sys

if __name__ == "__main__":

    myobj = {"email": sys.argv[2]}
    r = requests.post(sys.argv[1], data=myobj)
    g = requests.get(sys.argv[1])
    print(g.text)
