#!/usr/bin/python3
"""Gets total words in hot posts of a subreddit"""
import requests


def count_words(subreddit, keywords, cont='', obj={}):
    """ Gets total words in hot posts of a subreddit recursively"""

    if not obj:
        for k in keywords:
            if k.lower() not in obj:
                obj[k.lower()] = 0

    if cont is None:
        count = sorted(obj.items(), key=lambda y: (-y[1], y[0]))
        for w, c in count:
            if c:
                print('{}: {}'.format(w, c))
        return None

    link = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    h = {'user-agent': '0x16-api_advanced/0.0.1 (by /u/raytchellee)'}
    p = {'limit': 100, 'after': cont}

    response = requests.get(link,
                            headers=h,
                            params=p,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    try:
        hot_posts = response.json()['data']['children']
        next_token = response.json()['data']['after']
        for p in hot_posts:
            title = p['data']['title']
            lc = [word.lower() for word in title.split(' ')]

            for keyword in obj.keys():
                obj[keyword] += lc.count(keyword)

    except Exception:
        return None

    count_words(subreddit, keywords, next_token, obj)
