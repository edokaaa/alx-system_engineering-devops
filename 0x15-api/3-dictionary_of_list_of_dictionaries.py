#!/usr/bin/python3
"""Export to CSV.

A script that gathers data from an api and export it to json.
"""

import json
import requests


def get_all_todos():
    """Get the todos of a user."""
    todo_url = "https://jsonplaceholder.typicode.com/todos"

    todo_list = requests.get(todo_url).json()

    sorted_data = {}
    usernames = {}

    for entry in todo_list:
        user_id = str(entry['userId'])

        if user_id not in sorted_data:
            sorted_data[user_id] = []
            user_url = "https://jsonplaceholder.typicode.com/users/{}".format(
                user_id)
            user = requests.get(user_url).json()
            usernames[user_id] = user['username']

        sorted_data[user_id].append({
            "username": usernames[user_id],
            "task": entry['title'],
            "completed": entry['completed'],
        })
    return sorted_data


def export_json():
    """Export all todos to json."""
    data = get_all_todos()

    file_path = "todo_all_employees.json"
    with open(file_path, "w") as file:
        json.dump(data, file)


if __name__ == "__main__":
    export_json()
