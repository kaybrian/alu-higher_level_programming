#!/usr/bin/python3
"""Contect"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    """content"""
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            data = response.read()
            print(f"{data.decode('utf-8')}")
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
    except urllib.error.URLError as e:
        print(e.reason)
