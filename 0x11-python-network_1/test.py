#!/usr/bin/python3
""" takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter """

import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) < 2:
        q = ""
    else:
        q = argv[1]

    letter_search = {"q": q}
    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, letter_search)
    value_found = response.json()

    try:
        if value_found:
            print(f"{[value_found.get('id')]} {value_found.get('name')}")
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")
