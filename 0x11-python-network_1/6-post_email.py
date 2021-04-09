#!/usr/bin/python3
""" script to request a URL """

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    myobj = {"email": sys.argv[2]}
    r = requests.post(url, data=myobj)
    print(r.text)
