#!/bin/bash
# Bash script takes in a URL, sends request to that URL and displays the size of the body of the response
URL="$1"
curl -sGI "$URL" | grep "Content-Length" | cut -d " " -f 2
