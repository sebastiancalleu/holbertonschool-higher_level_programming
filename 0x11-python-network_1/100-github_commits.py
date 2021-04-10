#!/usr/bin/python3
"""script to get the last 10 commits"""
import requests
import sys


if __name__ == "__main__":
    session = requests.Session()
    session = session.get('https://api.github.com/repos/{}/{}/commits'.format(sys.argv[1], sys.argv[2]))
    if session.status_code == requests.codes.ok:
        jsondata = session.json()
        for i in range(10):
            print("{}: {}".format(jsondata[i]['sha'],
                                  jsondata[i]['commit']['author']['name']))
    session.close()
