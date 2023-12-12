#!/usr/bin/python3
"""Get subscribers count on a subreddit"""
import requests


def number_of_subscribers(subreddit):
    """Get subscribers count on a subreddit"""
    link = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    h = {
        "User-Agent": "0x16.api.advanced/0.0.1 (by /u/raytchellee)"
    }

    res = requests.get(link, headers=h, allow_redirects=False)
    if res.status_code == 404:
        return 0
    data = res.json().get("data")
    return data.get("subscribers")
