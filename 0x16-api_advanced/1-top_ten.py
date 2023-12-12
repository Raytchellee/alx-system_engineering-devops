#!/usr/bin/python3
""" Gets subreddit top ten """
import requests


def top_ten(subreddit):
    """ prints the titles of the first 10 hot posts """
    link = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    h = {'User-agent': '0x16-api_advanced/0.0.1 (by /u/raytchellee)'}
    p = {"limit": 10}

    res = requests.get(link, headers=h,
                       params=p, allow_redirects=False)
    if res.status_code == 200:
        for data in res.json().get('data').get('children'):
            print(data.get('data').get('title'))
    else:
        print("None")
