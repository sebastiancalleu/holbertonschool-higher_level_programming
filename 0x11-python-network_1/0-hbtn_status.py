#!/usr/bin/python3
""" script to request a URL """

import urllib.request

with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    the_page = response.read()
print("Body response:")
print("\t- type: ", type(the_page))
print("\t- content: ", the_page)
print("\t- utf8 content:", the_page.decode("UTF-8"))
