#!/usr/bin/python3
"""
fetches https://alx-intranet.hbtn.io/status using urllib
"""

import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as reply:
        res = reply.read()
        print('Body reply:')
        print("\t- type: {}".format(type(res)))
        print("\t- content: {}".format(res))
        print("\t- utf8 content: {}".format(res.decode('utf-8')))
