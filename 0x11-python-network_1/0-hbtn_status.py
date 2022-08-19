#!/usr/bin/python3
"""Script to make a get request"""


def main():
    """Entry point"""
    import urllib.request as req

    r = req.Request('https://intranet.hbtn.io/status')
    with req.urlopen(r) as response:
        body = response.read()
        print(f"""Body response:
        - type: {type(body)}
        - content: {body}
        - utf8 content: {body.decode()}""")


if __name__ == '__main__':
    main()
