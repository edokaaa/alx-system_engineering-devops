#!/usr/bin/python3
"""Export to CSV.

A script that gathers data from an api and export it to csv.
"""

import json
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


def export_csv():
    """Export user todo to csv."""
    todos, username = get_user_todos(user_id)
    file_path = "{}.csv".format(user_id)
    with open(file_path, "w") as file:
        for item in todos:
            line = '"{}","{}","{}","{}"\n'.format(
                user_id, username, item['completed'], item['title']
            )
            file.write(line)


def export_json(user_id):
    """Export user todo to json."""
    todos, username = get_user_todos(user_id)

    user_id = str(user_id)
    res = {
        user_id: []
    }

    for item in todos:
        todo = {
            "task": item["title"],
            "completed": item["completed"],
            "username": username
        }
        res[user_id].append(todo)
    file_path = "{}.json".format(user_id)
    with open(file_path, "w") as file:
        json.dump(res, file)


if __name__ == "__main__":
    try:
        user_id = sys.argv[1]
    except ValueError:
        print("User ID must be integer")
        exit(1)

    export_json(user_id)
