#!/usr/bin/python3
""" script to request a URL """

import requests
import requests.auth
import sys


if __name__ == "__main__":
    r = requests.get('https://api.github.com/user', auth=(sys.argv[1], sys.argv[2]))
    print(r.json()['id'])
