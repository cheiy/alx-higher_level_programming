#!/usr/bin/python3
'''
Script takes in a URL and an email address, sends a POST request
to the passed URL with the email address as a parameter and displays
the body response (decode in utf-8)
'''

if __name__ == "__main__":
    from sys import argv
    import urllib.request
    import urllib.parse

    url = argv[1]
    email_address = argv[2]
    email = urllib.parse.quote(email_address)
    email = email.encode('ascii')
    req = urllib.request.Request(url, email)
    with urllib.request.urlopen(req) as response:
        our_data = response.read().decode('utf-8')
    print(our_data)
