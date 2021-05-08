#!/usr/bin/python3
"""Export data into the Json format"""

import requests
import sys
import json

if __name__ == '__main__':
    endpoint = "https://jsonplaceholder.typicode.com/"
    userId = sys.argv[1]
    user = requests.get(endpoint + 'users/{}'.format(userId)).json()
    todo = requests.get(endpoint + 'todos?userId={}'.format(userId)).json()

    with open("{}.json".format(userId), 'w') as json_file:
        json.dump({
            userId:
                [{
                    "task": task.get("title"),
                    "completed": task.get("completed"),
                    "username": user.get("username")}
                 for task in todo]},
            json_file)
