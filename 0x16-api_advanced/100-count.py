#!/usr/bin/python3
""" Module for a recursive function that queries the Reddit API and counts keywords."""
import requests

def count_words(subreddit, word_list, after=None, counts=None):
    """ Recursive function to count keywords in hot articles on Reddit.

    Args:
        subreddit (str): The subreddit to query.
        word_list (list): List of keywords to count.
        after (str): Token for pagination in the query.
        counts (dict): Dictionary to store counts of keywords.

    Returns:
        None: Prints sorted counts of keywords in descending order by count and alphabetically for ties.
    """

    if counts is None:
        counts = {}

    if after is None:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print('{}: {}'.format(word, count))
        return

    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    headers = {'User-Agent': 'myRedditBot'}
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        print("Invalid subreddit or no posts match.")
        return

    try:
        hot_posts = response.json()['data']['children']
        next_token = response.json()['data']['after']
        for post in hot_posts:
            title = post['data']['title'].lower()
            for word in word_list:
                counts[word] = counts.get(word, 0) + title.count(word.lower())

    except Exception as e:
        print(e)
        return

    count_words(subreddit, word_list, next_token, counts)
