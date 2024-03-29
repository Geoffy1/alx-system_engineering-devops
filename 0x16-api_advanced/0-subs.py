#!/usr/bin/python3
"""
Query Reddit API for NO OF subscribers for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
        return NO OF subscribers for a given subreddit
        return 0 if invalid
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})

    r = requests.get(url, headers=headers).json()
    subscribers = r.get('data', {}).get('subscribers')
    if not subscribers:
        return 0
    return subscribers
