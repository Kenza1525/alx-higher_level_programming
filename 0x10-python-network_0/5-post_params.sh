#!/bin/bash
# send a GET request to the URL, and displays the body of the response.
curl -s -X POST -F "email=hr@holbertonschool.com" -F "subject=I will always be here for PLD" "$1"
