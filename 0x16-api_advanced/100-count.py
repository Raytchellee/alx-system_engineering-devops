#!/usr/bin/python3
"""Gets total words in hot posts of a subreddit"""
from requests import get


def count_words(subreddit, target_words, cont="", obj=None):
    """
    Gets total words in hot posts of a subreddit recursively.
    If no result return nothing
    """
    if obj is None:
        obj = {word: 0 for word in target_words}

    if cont is None:
        target_words_sorted = sorted(obj.items(), key=lambda x: (-x[1], x[0]))
        for word, count in target_words_sorted:
            if count:
                print(f"{word.lower()}: {count}")
        return None

    link = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    p = {
        'limit': 100,
        'after': cont
    }
    h = {
        'user-agent': '0x16-api_advanced/0.0.1 (by /u/raytchellee)'
    }
    res = get(link,
              headers=h,
              params=p,
              allow_redirects=False)

    if res.status_code != 200:
        return None

    try:
        json_data = res.json()
    except ValueError:
        return None

    try:
        result = json_data.get("data")
        props = result.get("children")
        next_page = result.get("after")
        for prop in props:
            post = prop.get("data")
            title = post.get("title")
            lowercased_words = [word.lower() for word in title.split(' ')]

            for word in target_words:
                obj[word] += lowercased_words.count(word.lower())
    except:
        return None

    count_words(subreddit, target_words, next_page, obj)
