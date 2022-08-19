#!/usr/bin/python3
"""Script to access the GitHub API"""


if __name__ == '__main__':
    import requests
    from sys import argv

    kwargs = {
        'url': 'https://api.github.com/repos/{}/{}/commits'
        .format(argv[2], argv[2])
    }
    response = requests.get(**kwargs)
    j = response.json()
    for i in range(10):
        print("{}: {}".
              format(j.get("sha"), j.get("commit").get("author").get('name')))
