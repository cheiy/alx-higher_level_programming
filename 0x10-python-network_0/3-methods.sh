#!/bin/bash
# Script displays all HTTP methods accepted by server
curl -s -IL -X OPTIONS "$1" | grep "Allow" | cut -d " " -f 2-
