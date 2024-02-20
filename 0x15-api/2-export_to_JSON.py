#!/usr/bin/python3
"""this module  to export data in the json format"""

import json
import requests
import sys


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/users"
    user_id = int(sys.argv[1])
    url = f"{base_url}/{user_id}"
    user_data = requests.get(url).json()
    user_name = user_data["username"]
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    file_name = "{}.json".format(user_id)
    user_tasks = []
    for task in todos:
        if task.get("userId") == int(user_id):
            user_tasks.append({"task": task["title"],
                               "completed": task["completed"],
                               "username": user_name})
    data = {str(user_id): user_tasks}
    with open(file_name, "w", newline='') as f:
        writer = json.dump(data, f)
