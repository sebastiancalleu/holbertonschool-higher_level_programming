#!/usr/bin/python3
""" script to request a URL """

import urllib.request

if __name__ == "__main__":

    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        headers = response.info()
        print(headers['X-Request-Id'])
