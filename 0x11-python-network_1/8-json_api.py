#!/usr/bin/python3
'''
Script takes a letter & sends POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
'''

if __name__ == "__main__":
    import requests
    from sys import argv

    url = "http://8a52a8698705.1e4c4cfb.alx-cod.online:5000/search_user"
    try:
        letter = argv[1]
    except IndexError:
        letter = {'q': ""}
        response = requests.post(url, data=letter)
    else:
        response = requests.post(url, data=letter)
    try:
        res_json = response.json()
    except HTTPError as e:
        print("No result")
    except JSONDecodeError as e:
        print("Not a valid JSON")
    else:
        i = response.json()['id']
        name = response.json()['name']
        print("[{}] {}".format(i, name))
