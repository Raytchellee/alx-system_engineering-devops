#!/usr/bin/python3
""" Module for a function that queries the Reddit API recursively."""

import requests

def count_words(subreddit, keywords, after='', word_count={}):
    """ Queries the Reddit API, parses hot article titles, and prints sorted counts of given keywords"""

    if not word_count:
        for keyword in keywords:
            if keyword.lower() not in word_count:
                word_count[keyword.lower()] = 0

    if after is None:
        sorted_counts = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            if count:
                print('{}: {}'.format(word, count))
        return None

    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    header = {'user-agent': 'redquery'}
    parameters = {'limit': 100, 'after': after}
    response = requests.get(url, headers=header, params=parameters, allow_redirects=False)

    if response.status_code != 200:
        return None

    try:
        hot_posts = response.json()['data']['children']
        next_token = response.json()['data']['after']
        for post in hot_posts:
            title = post['data']['title']
            lowercase_words = [word.lower() for word in title.split(' ')]

            for keyword in word_count.keys():
                word_count[keyword] += lowercase_words.count(keyword)

    except Exception:
        return None

    count_words(subreddit, keywords, next_token, word_count)
