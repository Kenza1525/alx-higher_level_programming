#!/bin/bash
# sent a get request to the url and display the body of the response
curl -sX GET -H "X-HolbertonSchool-User-Id: 98" "$1"
