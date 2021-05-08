#!/usr/bin/python3
"""Getting from API placeholder"""

import requests
import sys

if __name__ == '__main__':
    req_endpoint = "https://jsonplaceholder.typicode.com/"
    userId = sys.argv[1]
    user = requests.get(
        req_endpoint + 'users/{}'.format(userId), verify=False).json()

    todos = requests.get(
        req_endpoint + 'todos?userId={}'.format(userId), verify=False).json()

    completed = []
    for task in todos:
        if task.get("completed"):
            completed.append(task.get("title"))

    print("Employee {} is done with task({}/{}):"
          .format(user.get('name'), len(completed), len(todos)))

    for task in completed:
        print('\t', task)
