#!/bin/bash
#sends a JSON POST request to a URL and displays the body response
curl -sH "Content-Type: application/json" --request POST --data @"$2" "$1"
