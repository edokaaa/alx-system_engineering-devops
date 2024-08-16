#!/usr/bin/python3
"""How many subs?."""
import requests


def top_ten(subreddit):
    """Query the Reddit API and prints the titles \
of the first 10 hot posts listed for a given subreddit.

    Args:
        subreddit (str) - the id of the reddit user.

    """
    headers = {
        "User-agent": "ubuntu:alxse:v1.0 (by /u/edokadev)"
    }
    url = "https://www.reddit.com/r/{}/hot.json?limit=9".format(subreddit)
    res = requests.get(url, headers=headers,
                       allow_redirects=False)
    if res.status_code == 200:
        posts = res.json().get('data', {}).get('children', [])

        for post in posts:
            print(post['data']['title'])
    else:
        print(None)
