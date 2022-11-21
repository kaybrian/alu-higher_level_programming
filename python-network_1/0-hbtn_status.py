#!/usr/bin/python3
import urllib.request

res = urllib.request.Request("https://alu-intranet.hbtn.io/status")
with urllib.request.urlopen(res) as resp:
    data = resp.read()
    print("Body response:")
    print(f"\t- type:{type(data)}")
    print(f"\t- content:{data}")
    print(f"\t- utf8 content:{data.decode('utf-8')}")