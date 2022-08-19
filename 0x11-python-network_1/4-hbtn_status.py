#!/usr/bin/python3
"""Script to make a get request"""

if __name__ == '__main__':
    import requests
    response = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
