#!/usr/bin/python3
'''
Script takes in a URL and an email address, sends a POST request
to the passed URL with the email address as a parameter and displays
the body response (decode in utf-8)
'''

if __name__ == "__main__":
    from sys import argv
    import urllib.request

    url = argv[1]
    email_address = argv[2]
    '''data = urllib.parse.urlencode(email_address)
    data = data.encode('ascii')
    '''
    req = urllib.request.Request(url, email_address)
    with urllib.request.urlopen(req) as response:
        our_data = response.read()
    print(our_data)
