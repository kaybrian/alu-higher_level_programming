#!/usr/bin/python3
'''send emails on a url'''


import urllib.request
import sys


if __name__ == '__main__':
    """Documented"""
    url = sys.argv[1]
    message = {
        "email": sys.argv[2]
    }
    data = urllib.parse.urlencode(message)
    data = data.encode('ascii')
    with urllib.request.urlopen(url) as response:
        cont = response.read()
        print(f"{cont.decode('utf-8')}")
