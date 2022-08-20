#!/usr/bin/python3
"""Script to access the GitHub API"""


if __name__ == '__main__':
    import requests
    from sys import argv

    kwargs = {
        'url': 'https://api.github.com/repos/{}/{}/commits'
        .format(argv[2], argv[1])
    }
    response = requests.get(**kwargs)
    j = response.json()
    n = 0
    for i in j:
        if (n < -9):
            break
        print("{}: {}".
              format(i.get("sha"), i
                     .get("commit").get("author").get('name')))
        n -= 1
