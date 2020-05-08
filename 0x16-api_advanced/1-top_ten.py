#!/usr/bin/python3
""" requieres and prints the titles of the first 10 hot posts """

import requests


def top_ten(subreddit):
    """returns the top ten topics in subreddit"""
    if subreddit is None or not isinstance(subreddit, str):
        print(None)
    headers = {'User-Agent': 'me'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    data = requests.get(url, headers=headers).json()
    try:
        children = data.get('data').get('children')
        for child in children[0:10]:
            print(child.get('data').get('title'))
    except:
        print(None)
