#!/usr/bin/python3
"""Script to make a request to a given url and handles HTTP errors"""


if __name__ == '__main__':
    import requests
    from sys import argv

    response = requests.get(argv[1])
    s_code = response.status_code
    if (s_code >= 400):
        print(f"Error code: {s_code}")
    else:
        print(response.text)
