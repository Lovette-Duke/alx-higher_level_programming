#!/usr/bin/python3
"""
use Github API to list last 10 commits
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        argv[2], argv[1])
    res = requests.get(url)
    commits = res.json()
    for c in commits[0:10]:
        print(c.get('sha'), end=': ')
        print(c.get('commit').get('author').get('name'))
