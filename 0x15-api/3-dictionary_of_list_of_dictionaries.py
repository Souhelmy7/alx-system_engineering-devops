#!/usr/bin/python3
"""this module  to export data in the json format"""

import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"
    user_data = requests.get(url).json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    user_tasks = {}
    for user in user_data:
        user_id = str(user.get('id'))
        taskList = []
        for task in todos:
            if task.get('userId') == user.get('id'):
                taskDict = {"username": user.get('username'),
                            "task": task.get('title'),
                            "completed": task.get('completed')}
                taskList.append(taskDict)
        user_tasks[user_id] = taskList

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(user_tasks, f)
