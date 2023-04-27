#!/bin/bash
# Script sends a DELETE request to URL passed in 1st argument & displasy the body of the response.
curl -sX DELETE "$1"
