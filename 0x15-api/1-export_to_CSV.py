#!/usr/bin/python3
"""Export data into the CSV format"""

import requests
import sys
import csv

if __name__ == '__main__':
    endpoint = "https://jsonplaceholder.typicode.com/"
    userId = sys.argv[1]
    user = requests.get(endpoint + 'users/{}'.format(userId)).json()
    todo = requests.get(endpoint + 'todos?userId={}'.format(userId)).json()

    with open("{}.csv".format(userId), 'w', newline='') as csvfile:
        write_to_file = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todo:
            write_to_file.writerow([int(userId), user.get(
                'username'), task.get('completed'), task.get('title')])
