#!/usr/bin/python3
'''
This script fetches https://alx-intranet.hbtn.io/status
'''

if __name__ == "__main__":
    import urllib.request
    '''url = "https://alx-intranet.hbtn.io/status"'''
    url = argv[1]
    with urllib.request.urlopen(url2) as response:
        status = response.read()
    print("Body response:")
    print(" - type: {}".format(type(status)))
    print(" - content: {}".format(status))
    print(" - utf8 content: {}".format(status.decode('utf-8')))
