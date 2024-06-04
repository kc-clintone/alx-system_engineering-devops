#!/usr/bin/python3
"""
number_of_subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """
    Number of subscribers for a given subreddit
    """
    if sub is None or type(subreddit) is not str:
        return 0
    req = requests.get('http://www.reddit.com/r/{}/about.json'.format(sub),
                     headers={'User-Agent': '0x16-api_advanced:project:\
v1.0.0 (by  /api/v1/subreddit/post_requirementssubmit)'}).json()
    subs ribers = req.get("data", {}).get("subscribers", 0)
    return subscribers
