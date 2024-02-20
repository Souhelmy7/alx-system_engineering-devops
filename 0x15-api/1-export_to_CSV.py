#!/usr/bin/python3
"""this module  to export data in the CSV format"""

import csv
import requests
import sys


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/users"
    user_id = int(sys.argv[1])
    url = f"{base_url}/{user_id}"
    user_data = requests.get(url).json()
    user_name = user_data["username"]
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    file_name = "{}.csv".format(user_id)
    data = []
    for task in todos:
        if task.get("userId") == int(user_id):
            user_info = [user_id, user_name,
                         str(task.get("completed")), task.get("title")]
            data.append(user_info)
    with open(file_name, "w", newline='') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL, lineterminator='\n')
        writer.writerows(data)
