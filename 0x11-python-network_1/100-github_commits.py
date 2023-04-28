#!/usr/bin/python3
""" takes 2 arguments in order to solve a backend challenge """

import requests
from sys import argv

if __name__ == "__main__":
    repo = argv[1]
    owner = argv[2]
    url = f'https://api.github.com/repos/{repo}/{owner}/commits'
    response = requests.get(url)
    commits = response.json()
    for i in range(0, 10):
        print(f"{commits[i]['sha']} {commits[i]['commit']['author']['name']}")
