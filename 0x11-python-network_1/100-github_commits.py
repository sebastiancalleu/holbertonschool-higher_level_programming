#!/usr/bin/python3
"""script to get the last 10 commits"""
import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
    r = requests.get(url)
    if r.status_code == requests.codes.ok:
        for i in range(10):
            print("{}: {}".format(r.json()[i]['sha'],
                                  r.json()[i]['commit']['author']['name']))
