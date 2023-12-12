#!/usr/bin/python3
"""Gets total words in hot posts of a subreddit"""
import requests


def count_words(subreddit, word_list, obj={}, next="", idx=0):
    """Gets total number of words in hot posts of a subreddit"""
    link = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    h = {"User-Agent": "0x16-api_advanced/0.0.1 (by /u/raytchellee)"}
    p = {
        "limit": 100,
        "count": idx,
        "after": next,
    }

    res = requests.get(link,
                       headers=h,
                       params=p,
                       allow_redirects=False)

    try:
        data = res.json()
        if res.status_code == 404:
            raise Exception
    except Exception:
        print("")
        return

    data = data.get("data")
    next = data.get("after")
    idx += data.get("dist")

    for item in data.get("children"):
        t = item.get("data").get("title").lower().split()
        for elem in word_list:
            if elem.lower() in t:
                total = len([i for i in t if i == elem.lower()])
                if obj.get(elem) is not None:
                    obj[elem] += total
                else:
                    obj[elem] = total

    if next is None:
        if len(obj) == 0:
            print("")
            return
        obj = sorted(obj.items(), key=lambda x: (-x[1], x[0]))
        [print("{}: {}".format(a, b)) for a, b in obj]
    else:
        count_words(subreddit, word_list, obj, next, idx)
