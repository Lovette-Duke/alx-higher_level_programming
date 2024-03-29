#!/usr/bin/python3
"""
takes a url, sends a request to the URL
and displays the value of the X-Request-Id variable
"""
import urllib.request
from sys import argv


if __name__ == "__main__":
    res = urllib.request.Request(argv[1])
    with urllib.request.urlopen(res) as response:
        print(response.getheader('X-Request-Id'))
