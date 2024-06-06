#!/usr/bin/python3
"""
This function queries the Reddit API, returns the number of
subscribers for a given subreddit.
"""

import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """
    This function queries the Reddit API, returns the number of
    subscribers for a given subreddit.
    """
    if counts is None:
        counts = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        'User-Agent': 'python:subreddit.word.counter:v1.0 \
                       (by /u/Particular-Cattle673)'
    }
    params = {'limit': 100}
    if after:
        params['after'] = after

    try:
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)
        if response.status_code != 200:
            return

        data = response.json()
        posts = data['data']['children']
        for post in posts:
            title = post['data']['title'].lower()
            for word in word_list:
                word_lower = word.lower()
                word_count = title.split().count(word_lower)
                if word_count > 0:
                    if word_lower in counts:
                        counts[word_lower] += word_count
                    else:
                        counts[word_lower] = word_count

        after = data['data']['after']
        if after:
            count_words(subreddit, word_list, after, counts)
        else:
            sorted_counts = sorted(counts.items(),
                                   key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")

    except requests.RequestException:
        return
