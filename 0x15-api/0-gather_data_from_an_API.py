#!/usr/bin/python3
"""
 requesting employee's TODO list using his/her ID.
"""

import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    users_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    name_req = requests.get(users_url).json()
    name = name_req.get("name")

    params = {"userId": int(user_id)}
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    todo_list = requests.get(todos_url, params=params).json()
    completed = 0
    lst = []
    for item in todo_list:
        if item.get("completed") is True:
            completed += 1
            lst.append(item.get("title"))

    print("Employee {} is done with tasks({}/{}):".format(
        name, completed, len(todo_list)))
    for i in lst:
        print("\t {}".format(i))
