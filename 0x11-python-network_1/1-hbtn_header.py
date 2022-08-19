#!/usr/bin/python3
"""Script to make a get request to a given url and print a specific header"""
import urllib.request as req
from sys import argv

r = req.Request(argv[1])
with req.urlopen(r) as response:
    print(response.getheader('X-Request-Id'))
