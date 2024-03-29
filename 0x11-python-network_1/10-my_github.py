#!/usr/bin/python3
"""
takes a GitHub credentials and uses
GitHub API to display the associated id
"""
import requests
from requests.auth import HTTPBasicAuth
from sys import argv


if __name__ == "__main__":
    a = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    url = "https://api.github.com/user"
    res = requests.get(url, auth=a)
    print(res.json().get("id"))
