#!/usr/bin/python3
"""
fetches https://alx-intranet.hbtn.io/status using urllib
"""

import urllib.request

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        res = response.read()
        print('Body response:')
        print("    - type: {}".format(type(res)))
        print("    - content: {}".format(res))
        print("    - utf8 content: {}".format(res.decode('utf-8')))
