#!/usr/bin/python3
"""A script that gathers data from an api."""

import sys
import requests

user_id = int(sys.argv[1])
todo_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(user_id)
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
    exit (1)

print("Employee {} is done with tasks({}/{})".format(user["name"], len(completed), total_task))
for item in completed:
    print("\t {}".format(item))

