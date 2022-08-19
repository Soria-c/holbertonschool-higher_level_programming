#!/usr/bin/python3
"""Script to make a post request to a given url"""
import urllib.request as req
import urllib.parse as parse_data
from sys import argv


def main():
    """Entry point"""

    payload = {
        'email': argv[2]
    }

    kwargs = {
        'url': argv[1],
        'data': parse_data.urlencode(payload).encode()
    }
    r = req.Request(**kwargs)
    with req.urlopen(r) as response:
        print(response.read().decode())


if __name__ == '__main__':
    main()
