#!/usr/bin/python3
"""Script to access the GitHub API"""


if __name__ == '__main__':
    import requests
    from sys import argv

    kwargs = {
        'url': f'https://api.github.com/repos/{argv[1]}/{argv[2]}/commits'
    }
    response = requests.get(**kwargs)
    for i in response.json():
        print(i.get("sha"), i.get("commit").get("author").get('name'))
