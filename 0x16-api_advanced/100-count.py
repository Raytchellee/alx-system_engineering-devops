#!/usr/bin/python3
"""Gets total words in hot posts of a subreddit"""
from requests import get


def count_words(subreddit, word_list, cont="", obj={}):
    """
    Gets total words in hot posts of a subreddit recursively.
    If no result return nothing
    """

    if not obj:
        for word in word_list:
            obj[word] = 0

    if cont is None:
        word_list = [[a, b] for a, b in obj.items()]
        word_list = sorted(word_list, key=lambda y: (-y[1], y[0]))
        for word in word_list:
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
        next = result.get("after")
        props = result.get("children")
        for prop in props:
            post = prop.get("data")
            t = post.get("title")
            lc = [word.lower() for word in t.split(' ')]

            for word in word_list:
                obj[word] += lc.count(word.lower())
    except:
        return None

    count_words(subreddit, word_list, next, obj)
