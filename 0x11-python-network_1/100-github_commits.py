#!/usr/bin/python3
"""script to get the last 10 commits"""
import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(repo, owner)
    session = requests.Session()
    session = session.get(url)
    if session.status_code == requests.codes.ok:
        jsondata = session.json()
        for i, obj in enumerate(jsondata):
            if i == 10:
                break
            print("{}: {}".format(obj['sha'],
                                  obj['commit']['author']['name']))
    session.close()
