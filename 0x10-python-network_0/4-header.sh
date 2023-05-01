#!/bin/bash
# Script takes in a URL, sends a GET request to the URL & displays the body
curl -sG -H "X-School-User-Id: 98" "$1"
