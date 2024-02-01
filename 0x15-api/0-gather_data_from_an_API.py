#!/usr/bin/python3
"""Gather data from an API.

A script that gathers data from an api.
"""

import requests
import sys


def user_todos(user_id):
    """Get the todos of a user."""
    todo_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        user_id)
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)

    todo_list = requests.get(todo_url).json()
    user = requests.get(user_url).json()

    total_task = len(todo_list)
    completed = []

    for todo in todo_list:
        if todo['completed']:
            completed.append(todo['title'])
    try:
        username = user["name"]
    except KeyError as e:
        print("User not found")
        exit(1)

    print("Employee {} is done with tasks({}/{}):".format(
        user["name"], len(completed), total_task))
    for item in completed:
        print("\t {}".format(item))


if __name__ == "__main__":
    try:
        user_id = sys.argv[1]
    except ValueError:
        print("User ID must be integer")
        exit(1)

    user_todos(user_id)
