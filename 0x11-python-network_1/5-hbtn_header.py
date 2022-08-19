#!/usr/bin/python3
"""Script to make a get request to a given url and print a specific header"""


if __name__ == '__main__':
    import requests
    from sys import argv

    response = requests.get(argv[1])
    print(response.headers.get('X-Request-Id'))
