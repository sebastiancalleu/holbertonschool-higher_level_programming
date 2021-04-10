#!/usr/bin/python3
"""script to get the last 10 commits"""
import requests
import sys


if __name__ == "__main__":
    url = 'https://api.github.com/repos/{}/{}/commits'.format(sys.argv[2], sys.argv[1])
    r = requests.get(url)
    if r.status_code == 200:
        for i in range(10):
            print("{}: {}".format(r.json()[i]['sha'],
                                  r.json()[i]['commit']['author']['name']))
