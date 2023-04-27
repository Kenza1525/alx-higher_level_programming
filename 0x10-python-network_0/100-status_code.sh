#!/bin/bash
#sends a request as an argument to an URL and displays only the status code
curl -s -o /dev/null -w "%{http_code}" "$1"
