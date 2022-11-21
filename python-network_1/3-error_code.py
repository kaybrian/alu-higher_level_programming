#!/usr/bin/python3
"""displays the body of the response"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    """module to display content"""
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
