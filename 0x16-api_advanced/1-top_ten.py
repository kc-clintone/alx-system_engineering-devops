#!/usr/bin/python3
"""
Count top ten posts
"""

import requests


def top_ten(subreddit):
    """
    Returns top ten hot posts
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {
        'User-Agent': 'python:subreddit.hot.posts:v1.0 (by /u/Particular-Cattle673)'
    }
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                print(post['data']['title'])
        else:
            print(None)
    except requests.RequestException:
        print(None)
