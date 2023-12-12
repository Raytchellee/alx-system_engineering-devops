#!/usr/bin/python3
"""Rinse and repeat list of hot posts"""
import requests


def recurse(subreddit, hot_list=[], next="", idx=0):
    """gets all the top hot posts"""
    link = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    h = {"User-Agent": "0x16-api_advanced/0.0.1 (by /u/raytchellee)"}
    p = {
        "limit": 100,
        "count": idx,
        "after": next
    }

    res = requests.get(link,
                       headers=h,
                       params=p,
                       allow_redirects=False)

    if res.status_code == 404:
        return None

    data = res.json().get("data")
    next = data.get("after")
    idx += data.get("dist")
    for item in data.get("children"):
        hot_list.append(item.get("data").get("title"))

    if next is not None:
        return recurse(subreddit, hot_list, next, idx)

    return hot_list
