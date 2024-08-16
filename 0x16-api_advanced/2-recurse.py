#!/usr/bin/python3

"""Returns a list containing all hot articles for a given subreddit."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Return a list containing all hot articles for a given subreddit.

    Args:
        subreddit(str): Subreddit
        hot_list(llist): List of titles
        after(str): Fullname of item to use as starting point for next slice
    Return:
        (list of str): List of all hot articles or None on error.
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {
        "User-agent": "ubuntu:alxse:v1.0 (by /u/edokadev)"
    }
    params = {'limit': 100}

    if after:
        params['after'] = after

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json()

        # Extract posts
        posts = data['data']['children']

        # add posts to hot list
        hot_list += posts

        after = data['data']['after']
        if after:
            # Recursively fetch remaining hot posts
            hot_list = recurse(subreddit, hot_list, after)

        # Return list of titles after all hot posts have been fetched
        return hot_list
    return None
