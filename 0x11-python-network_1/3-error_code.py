#!/usr/bin/python3
"""Script to make a request to a given url and handles HTTP errors"""
import urllib.request as req
import urllib.error
from sys import argv


def main():
    """Entry point"""
    r = req.Request(argv[1])
    try:
        with req.urlopen(r) as response:
            print(response.read().decode())
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")


if __name__ == '__main__':
    main()
