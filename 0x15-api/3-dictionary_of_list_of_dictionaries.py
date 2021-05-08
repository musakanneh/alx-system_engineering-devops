#!/usr/bin/python3
"""Dictionary of list of dictionaries"""

import json
import requests

if __name__ == '__main__':
    endpoint = requests.get('https://jsonplaceholder.typicode.com/users')
    users = endpoint.json()
    endpoint = requests.get('https://jsonplaceholder.typicode.com/todos')
    task = endpoint.json()

    dic = {
        str(data.get('id')): [
            {
                'username': data.get('username'),
                'task': item .get('titles'), 'completed':
                    item.get('completed')
            }
            for item in task
            if item.get('userId') == data.get('id')
        ]
        for data in users
    }
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(dic, json_file)
