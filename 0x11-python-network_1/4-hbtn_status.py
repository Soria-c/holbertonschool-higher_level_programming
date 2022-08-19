#!/usr/bin/python3
"""Script to make a get request"""

if __name__ == '__main__':
    import requests
    response = requests.get("https://intranet.hbtn.io/status")
    print(f"""Body response:
        - type: {type(response.text)}
        - content: {response.text}""")
