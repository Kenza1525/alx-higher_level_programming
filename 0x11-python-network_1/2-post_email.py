#!/usr/bin/python3
""" takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays
the body of the response (decoded in utf-8) """

import urllib.request
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    email_dict = {"email": email}
    email_encode = urllib.parse.urlencode(email_dict)
    email_encode = email_encode.encode('ascii')
    request = urllib.request.Request(url, email_encode)

    with urllib.request.urlopen(request) as response:
        page = response.read()
        page_decode = page.decode('utf-8')
        print(page_decode)
