#!/usr/bin/python3
"""Export to CSV.

A script that gathers data from an api and export it to csv.
"""

import os
import requests
import sys


def get_user_todos(user_id):
    """Get the todos of a user."""
    todo_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        user_id)
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)

    todo_list = requests.get(todo_url).json()
    user = requests.get(user_url).json()

    try:
        username = user["username"]
    except KeyError as e:
        print("User not found")
        exit(1)
    return (todo_list, username)


if __name__ == "__main__":
    try:
        user_id = sys.argv[1]
    except ValueError:
        print("User ID must be integer")
        exit(1)

    # user_todos(user_id)
    todos, username = get_user_todos(user_id)

    file_path = "{}.csv".format(user_id)
    with open(file_path, "w") as file:
        for item in todos:
            line = '"{}","{}","{}","{}"\n'.format(
                user_id, username, item['completed'], item['title']
            )
            file.write(line)
