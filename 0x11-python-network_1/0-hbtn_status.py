#!/usr/bin/python3
"""Script to make a get request"""
if __name__ == "__main__":
    import urllib.request as req
    r = req.Request('https://intranet.hbtn.io/status')
    with req.urlopen(r) as response:
        body = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(body)))
        print('\t- content: {}'.format(body))
        print('\t- utf8 content: {}'.format(body.decode('utf-8')))
