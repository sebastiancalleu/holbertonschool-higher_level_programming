#!/usr/bin/python3
""" script to request a URL """

import urllib.request
import sys
import urllib.error

if __name__ == "__main__":

    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            the_page = response.read()
            print(the_page.decode("UTF-8"))
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.getcode()))
