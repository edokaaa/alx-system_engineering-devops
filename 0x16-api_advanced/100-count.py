#!/usr/bin/python3

"""Returns a list containing all hot articles for a given subreddit."""
import requests


def count_words(subreddit, word_list):
    """Recursive function that queries the Reddit API.

    parses the title of all hot articles,
    and prints a sorted count of given keywords

    Args:
        subreddit(str): Subreddit
        word_list(list): List of keywords.
    """
    def recurse_fetch(subreddit, hot_list=[], after=None):
        """Return a list containing all hot articles for a given subreddit.

        Args:
            subreddit(str): Subreddit
            hot_list(llist): List of titles
            after(str): Fullname of item to use as starting
            point for next slice
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
                hot_list = recurse_fetch(subreddit, hot_list, after)

            # Return list of titles after all hot posts have been fetched
            return hot_list
        return None

    """Count the occurance of the keywordword in the title recursively"

    Args:
        words(list): list of keywords
        title(str): title of post
    """
    def recursive_count(words, title):
        # Base case: if no words left, return
        if not words:
            return

        # Get the first word
        word = words[0].lower()

        # Check if the word is in the title
        if word in title.lower():
            # Increment the word count
            w_counts[word] = w_counts.get(word, 0) + title.lower().count(word)

        # Recursively call the function with the remaining words
        recursive_count(words[1:], title)

    hot_list = recurse_fetch(subreddit)

    if not hot_list:
        return

    w_counts = {}

    # Iterate over the articles and call the recursive function
    for article in hot_list:
        title = article['data']['title']
        recursive_count(word_list, title)

    # Sort and print the word counts
    sorted_counts = sorted(w_counts.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_counts:
        print(f"{word}: {count}")
