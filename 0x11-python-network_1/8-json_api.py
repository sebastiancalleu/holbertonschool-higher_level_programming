#!/usr/bin/python3
""" script to request a URL """

import requests
import sys


if __name__ == "__main__":
    if sys.argv[1]:
        myobj = {"q": sys.argv[1]}
    else:
        myobj = {"q": ""}
    r = requests.post('http://0.0.0.0:5000/search_user', data=myobj)
    print("[{}] {}".format(r.json()['id'], r.json()['name']))
