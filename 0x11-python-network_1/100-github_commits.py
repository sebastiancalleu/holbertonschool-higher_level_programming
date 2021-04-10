#!/usr/bin/python3
""" script to get the last 10 commits """

import requests
import sys


if __name__ == "__main__":
    count = 0
    session = requests.Session()
    session = session.get('https://api.github.com/repos/{}/{}/commits'.format(sys.argv[1], sys.argv[2]))
    if session.status_code == requests.codes.ok:
        for i in session.json():
            if count == 10:
                break
            print("{}: {}".format(i['sha'],
                                  i['commit']['author']['name']))
            count += 1
    session.close()
