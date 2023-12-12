#!/usr/bin/python3
"""Gets total words in hot posts of a subreddit"""
import requests


def count_words(subreddit, keywords, cont='', obj={}):
    """
    Gets total words in hot posts of a subreddit recursively.
    If no result return nothing
    """

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

    res = requests.get(link,
                            headers=h,
                            params=p,
                            allow_redirects=False)

    if res.status_code != 200:
        return None

    try:
        hot_posts = res.json()['data']['children']
        next_token = res.json()['data']['after']
        for p in hot_posts:
            title = p['data']['title']
            lc = [word.lower() for word in title.split(' ')]

            for keyword in obj.keys():
                obj[keyword] += lc.count(keyword)

    except Exception:
        return None

    count_words(subreddit, keywords, next_token, obj)

#!/usr/bin/python3
"""Gets total words in hot posts of a subreddit"""
from requests import get


def count_words(subreddit, target_words, cont="", obj={}):
    """
    Gets total words in hot posts of a subreddit recursively.
    If no result return nothing
    """

    if not obj:
        for word in target_words:
            obj[word] = 0

    if cont is None:
        target_words = [[a, b] for a, b in obj.items()]
        target_words = sorted(target_words, key=lambda y: (-y[1], y[0]))
        for word in target_words:
            if word[1]:
                print("{}: {}".format(word[0].lower(), word[1]))
        return None

    link = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    p = {
        'limit': 100,
        'after': cont
    }
    h = {
        'user-agent': '0x16-api_advanced/0.0.1 (by /u/raytchellee)'
    }
    res = get(link, headers=h, params=p, allow_redirects=False)

    if res.status_code != 200:
        return None
    try:
        json_data = res.json()
    except ValueError:
        return None

    try:
        result = json_data.get("data")
        props = result.get("children")
        next = result.get("after")
        for prop in props:
            post = prop.get("data")
            t = post.get("title")
            lc = [word.lower() for word in t.split(' ')]

            for word in target_words:
                obj[word] += lc.count(word.lower())
    except:
        return None

    count_words(subreddit, target_words, next, obj)
