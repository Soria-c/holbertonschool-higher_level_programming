#!/usr/bin/python3
"""Script to make a post request to get a json"""


if __name__ == '__main__':
    import requests
    from sys import argv

    kwargs = {
        'url': 'http://0.0.0.0:5000/search_user',
        'data': {
            'q': argv[1] if len(argv) >= 2 else ""
        }
    }

    response = requests.post(**kwargs)
    try:
        js_on = response.json()
        if (js_on):
            print(f"[{js_on.get('id')}] {js_on.get('name')}")
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
