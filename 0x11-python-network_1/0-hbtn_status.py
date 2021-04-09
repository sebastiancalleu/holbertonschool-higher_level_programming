#!/usr/bin/python3
""" script to request a URL """

import urllib.request

if __name__ == "__main__":

    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        the_page = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(the_page)))
    print("\t- content: {}".format(the_page))
    print("\t- utf8 content: {}".format(the_page.decode("UTF-8")))
