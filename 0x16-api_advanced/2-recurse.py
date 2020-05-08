#!/usr/bin/python3
""" Contains the list of all the topics """

import requests


def recurse(subreddit, hot_list=[], after=""):
    """returns the list of all hot topics in subreddit"""
    headers = {'User-Agent': 'me'}
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
        subreddit, after)
    data = requests.get(url, headers=headers).json()
    try:
        children = data.get('data').get('children')
        for child in children:
            hot_list.append(child.get('data').get('title'))
    except:
        return None
    after = data.get('data').get('after')
    if after is None:
        return (hot_list)
    return recurse(subreddit, hot_list, after)
