#!/usr/bin/python3
""" script to get the las 10 commits """

import requests
import sys


if __name__ == "__main__":
    r = requests.get('https://api.github.com/repos/{}/{}/commits'.format(sys.argv[1], sys.argv[2]))
    for i in range(10):
        print((r.json()[i]['sha']) + " " +
              (r.json()[i]['commit']['author']['name']))
