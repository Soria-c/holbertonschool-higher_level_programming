#!/usr/bin/python3
"""Script to make a post request to a given url"""


if __name__ == '__main__':
    import requests
    from sys import argv

    kwargs = {
        'url': argv[1],
        'data': {
            'email': argv[2]
        }
    }

    response = requests.post(**kwargs)
    print(response.text)
