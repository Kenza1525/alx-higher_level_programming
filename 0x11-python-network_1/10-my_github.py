#!/usr/bin/python3
"""  takes your GitHub credentials (username and password)
and uses the GitHub API to display your id """

import requests
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    p_a_t = argv[2]
    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(username, p_a_t))
    r_json = response.json()
    print(r_json.get('id'))
