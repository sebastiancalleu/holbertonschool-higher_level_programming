""" script to request a URL """

import urllib.request
import urllib
import sys

if __name__ == "__main__":

    email = urllib.parse.urlencode({"email": sys.argv[2]})
    email = email.encode("ascii")
    req = urllib.request.Request(sys.arv[1], email)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        print(the_page.decode("UTF-8"))
