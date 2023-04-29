#!/usr/bin/python3
'''
This script takes in a URL, sends a request to the URL and displays the body
of the response (decoded in utf-8)
'''

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import urllib.error
    from sys import argv

    url = argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            content = response.read().decode('utf-8')
            print(content)
    except urllib.error.HTTPError as e:
        print("Error Code: {}".format(e.code))
