#!/usr/bin/python3

import requests
import sys


if __name__ == "__main__":
    r = requests.get('https://api.github.com/repos/rails/rails/commits')
    for i in range(10):
        print((r.json()[i]['sha']) + " " +
              (r.json()[i]['commit']['author']['name']))
