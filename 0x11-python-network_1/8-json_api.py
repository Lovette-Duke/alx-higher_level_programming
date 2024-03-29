#!/usr/bin/python3
"""
Sends a POST with a given letter.
"""
import requests
from sys import argv


if __name__ == "__main__":
    alpha = "" if len(argv) == 1 else argv[1]
    load = {"q": alpha}

    res = requests.post("http://0.0.0.0:5000/search_user", data=load)
    try:
        response = res.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
