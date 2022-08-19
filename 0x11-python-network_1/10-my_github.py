#!/usr/bin/python3
"""Script to access the GitHub API"""


if __name__ == '__main__':
    import requests
    from sys import argv

    kwargs = {
        'url': 'https://api.github.com/user',
        'auth': (argv[1], argv[2])
    }
    response = requests.get(**kwargs)
    print(response.json().get('id'))
