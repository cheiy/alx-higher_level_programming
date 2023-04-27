#!/bin/bash
# Grep displays all HTTP methods accepted by server
curl -sI "%$" | grep "Allow" | cut -d ' ' -f 2
