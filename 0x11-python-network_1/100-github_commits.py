#!/usr/bin/python3
""" script to get the last 10 commits """

import requests
import sys


if __name__ == "__main__":
    r = requests.get('https://api.github.com/repos/{}/{}/commits'.format(sys.argv[1], sys.argv[2]))
    if r.status_code == 200:
        for i in range(10):
            print("{}: {}".format(r.json()[i]['sha'],
                                  r.json()[i]['commit']['author']['name']))
