#!/usr/bin/python3
"""
gathers data from API and exports it to JSON file
Implemented using recursion
"""
import json
import requests


ENDPOINT = "https://jsonplaceholder.typicode.com"
"""REST API url"""


if __name__ == '__main__':
    users = requests.get('{}/users'.format(ENDPOINT)).json()
    tds = requests.get('{}/todos'.format(ENDPOINT)).json()
    data = {}
    for user in users:
        usr_id = user.get('id')
        usr_name = user.get('username')
        todos = list(filter(lambda x: x.get('userId') == usr_id, tds))
        usr_data = list(map(
            lambda x: {
                'username': usr_name,
                'task': x.get('title'),
                'completed': x.get('completed')
            },
            todos
        ))
        data['{}'.format(usr_id)] = usr_data
    with open('todo_all_employees.json', 'w') as file:
        json.dump(data, file)
