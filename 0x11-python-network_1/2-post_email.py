#!/usr/bin/python3
"""
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response
"""
from sys import argv
import urllib.request
import urllib.parse


if __name__ == "__main__":
    url = argv[1]
    body = {'email': argv[2]}

    email = urllib.parse.urlencode(body)
    email = email.encode('ascii')
    res = urllib.request.Request(url, email)
    with urllib.request.urlopen(res) as response:
        print(response.read().decode('utf-8'))
