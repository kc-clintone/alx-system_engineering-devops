#!/usr/bin/python3
"""
Count
"""

import requests
from collections import Counter
import re


def count_words(subreddit, word_list, after=None, counter=None):
    """
    Counts top hot posts
    """
    if counter is None:
        counter = Counter()
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'python:subreddit.keyword.counter: \
               v1.0 (by /u/Particular-Cattle673)'}
    params = {'limit': 100}
    if after:
        params['after'] = after

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code != 200:
            return
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            title = post['data']['title']
            words_in_title = re.findall(r'\b\w+\b', title.lower())
            for word in word_list:
                counter[word.lower()] += words_in_title.count(word.lower())

        after = data['data'].get('after')
        if after:
            count_words(subreddit, word_list, after, counter)
        else:
            sorted_counts = sorted(counter.items(),
                                   key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                if count > 0:
                    print(f"{word}: {count}")
    except requests.RequestException:
        return
