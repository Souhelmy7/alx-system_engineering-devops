#!/usr/bin/python3
"""this module returns information about his/her todo list progress"""

import requests
import sys

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/users"
    user_id = int(sys.argv[1])
    url = f"{base_url}/{user_id}"
    user_data = requests.get(url).json()
    user_name = user_data["name"]

    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    total_tasks = 0
    completed_task = 0
    for task in todos:
        if task.get("userId") == int(user_id):
            total_tasks += 1
            if task.get("completed"):
                completed_task += 1
    output = "Employee {} is done with tasks({}/{}):".format(
        user_name, completed_task, total_tasks
    )
    print(output)
    for task in todos:
        if task.get("userId") == int(user_id) and task.get("completed"):
            title = task.get("title")
            formatted_title = f"\t {title}"
            print(formatted_title)
