#!/usr/bin/python3

import requests
import requests.auth
import sys


if __name__ == "__main__":
    r = requests.get('https://api.github.com/repos/rails/rails/commits')
    print(r.json())