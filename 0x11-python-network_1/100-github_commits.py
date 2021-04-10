#!/usr/bin/python3
"""script to get the last 10 commits"""
import requests
import sys


def main(url):
    """ make the request to API and get the last commits """
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

if __name__ == "__main__":
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner_name, repository_name)

    main(url)
