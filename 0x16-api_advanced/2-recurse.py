#!/usr/bin/python3
"""
Recurse.py
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursive request
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        'User-Agent': 'python:subreddit.hot.articles:v1.0 \
                       (by /u/Particular-Cattle673)'
    }
    params = {'limit': 100}
    if after:
        params['after'] = after

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code != 200:
            return None

        data = response.json()
        posts = data['data']['children']
        for post in posts:
            hot_list.append(post['data']['title'])

        after = data['data']['after']
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list if hot_list else None

    except requests.RequestException:
        return None
