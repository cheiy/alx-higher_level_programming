#!/usr/bin/python3
'''
This script takes in a URL and https://alx-intranet.hbtn.io/status
'''

if __name__ == "__main__":
    import urllib.request
    from sys import argv

    url = argv[1]

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        header = response.getheader('X-Request-Id')
    print(header)
