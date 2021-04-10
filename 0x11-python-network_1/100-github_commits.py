#!/usr/bin/python3
"""script to get the last 10 commits"""
import requests
import sys


if __name__ == "__main__":
    r = requests.get('https://api.github.com/repos/{}/{}/commits'.format
                     (sys.argv[2], sys.argv[1]))
    data = r.json()
    if r.status_code == requests.codes.ok:
        for i, obj in enumerate(data):
            if i == 10:
                break
            print("{}: {}".format(obj['sha'],
                                  obj['commit']['author']['name']))
