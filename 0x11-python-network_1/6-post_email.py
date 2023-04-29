#!/usr/bin/python3
'''
Script takes in a URL & an email address, sends a POST request to the URL
with the email as a parameter, & finally displasy the body of the response.
'''

if __name__ == "__main__":
    import requests
    from sys import argv

    url = argv[1]
    email_address = argv[2]
    payload = {'email': email_address}

    request = requests.post(url, data=payload)
    print(request.text)
