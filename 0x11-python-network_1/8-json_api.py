#!/usr/bin/python3
"""Sends POST request"""
import requests
from sys import argv
if __name__ == "__main__":
    if len(argv) < 2:
        arg = ""
    else:
        arg = argv[1]
    letter = {"q": arg}
    post = requests.post("http://0.0.0.0:5000/search_user", letter)
    try:
        json = post.json()
        if len(json) == 0:
            print("No result")
        else:
            print("[{}] {}".format(json.get('id'),
                                   json.get('name')))
    except ValueError:
        print("Not a valid JSON")
