#!/usr/bin/python3
""" Function that requies and return the number of subscribers """

import requests


def number_of_subscribers(subreddit):
    """ Return the numer of sbuscribers for a given subreddit """
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    headers = {'User-Agent': 'me'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    data = requests.get(url, headers=headers).json()
    try:
        return (data.get('data').get('subscribers'))
    except:
        return 0
