#!/usr/bin/python3
'''
Script takes a letter & sends POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
'''

if __name__ == "__main__":
    import requests
    from sys import argv

    url = "http://0.0.0.0:5000/search_user"
    try:
        letter = {'q': argv[1]}
        response = requests.post(url, data=letter)
    except IndexError:
        letter = {'q': ""}
        response = requests.post(url, data=letter)
    try:
        i = response.json()['id']
        name = response.json()['name']
        if i is None or name is None:
            print("Not a valid JSON")
            exit()
    except KeyError as ke:
        print("No result")
    else:
        print("[{}] {}".format(i, name))
