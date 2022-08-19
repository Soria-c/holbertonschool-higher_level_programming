#!/usr/bin/python3
"""Script to make a get request"""
if __name__ == "__main__":
    import urllib.request as req
    r = req.Request('https://intranet.hbtn.io/status')
    with req.urlopen(r) as response:
        body = response.read()
        print(f"""Body response:
        - type: {type(body)}
        - content: {body}
        - utf8 content: {body.decode()}""")
