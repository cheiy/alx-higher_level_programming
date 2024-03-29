#!/usr/bin/python3
'''
Script fetches https://alx-intranet.hbtn.io/status using the requests package
'''

if __name__ == "__main__":
    import requests

    url = "https://alx-intranet.hbtn.io/status"
    r = requests.get(url)
    print("Body response:")
    print("    - type: {}".format(type(r.reason)))
    print("    - content: {}".format(r.text))
