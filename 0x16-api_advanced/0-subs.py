#!/usr/bin/python3
"""How many subs?."""
import requests


def number_of_subscribers(subreddit):
    """Query the Reddit API.

    Args:
        subreddit (str) - the id of the reddit user.
    Returns:
        The number of subcribers for the subreddit.
    """
    headers = {
        "User-agent": "ubuntu:alxse:v1.0 (by /u/edokadev)"
    }
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    res = requests.get(url, headers=headers,
                       allow_redirects=False)
    if res.status_code == 200:
        data = res.json().get('data', [])

        if 'subscribers' in data:
            return data.get('subscribers')
    return 0
