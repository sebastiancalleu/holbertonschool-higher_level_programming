#!/usr/bin/python3
"""script to get the last 10 commits"""
import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
    session = requests.Session()
    session = session.get(url)
    data = session.json()
    if session.status_code == requests.codes.ok:
        for i in range(10):
            print("{}: {}".format(data[i]['sha'],
                                  data[i]['commit']['author']['name']))
