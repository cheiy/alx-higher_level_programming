#!/usr/bin/python3
'''
Script takes a URL, sends a request to the URL and displays the value of
the variable X-Request-Id in the response header.
'''

if __name__ == "__main__":
    import requests
    from sys import argv

    url = argv[1]
    header = 'X-Request-Id'
    response = requests.get(url)
    if response.headers.get(header) is not None:
        print(response.headers[header])
