#!/usr/bin/python3
'''a Python script that fetches a url'''


import urllib.request


if __name__ == '__main__':
    res = urllib.request.Request("https://alu-intranet.hbtn.io/status")
    with urllib.request.urlopen(res) as resp:
        data = resp.read()
        print("Body response:")
        print("\t- type: {}".format(type(data)))
        print("\t- content: {}".format(data))
        print("\t- utf8 content: {}".format(data.decode("utf-8")))
