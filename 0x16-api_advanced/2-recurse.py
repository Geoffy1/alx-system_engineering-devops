#!/usr/bin/python3
"""
Query Reddit API recursively for all hot articles present
"""
import requests


def recurse(subreddit, hot_list=[], after="tmp"):
    """
        return all hot articles
        returns None if invalid subreddit given
    """
    # get user agent
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})

    # updates url each recursive call with param "after"
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    if after != "tmp":
        url = url + "?after={}".format(after)
    r = requests.get(url, headers=headers, allow_redirects=False)

    # appending the top titles to hot_list
    results = r.json().get('data', {}).get('children', [])
    if not results:
        return hot_list
    for e in results:
        hot_list.append(e.get('data').get('title'))

    # gets the next param "after" else nothing else to recurse
    after = r.json().get('data').get('after')
    if not after:
        return hot_list
    return (recurse(subreddit, hot_list, after))
