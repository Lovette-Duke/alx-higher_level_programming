#!/usr/bin/python3
"""
takes in a URL and an email address,
sends a POST request to the passed URL with the email, and displays it
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    email = {"email": argv[2]}

    res = requests.post(url, data=email)
    print(res.text)
