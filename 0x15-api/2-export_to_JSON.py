#!/usr/bin/python3
"""
gathers data from API and exports it to JSON file
Implemented using recursion
"""
import json
import re
import requests
import sys


ENDPOINT = "https://jsonplaceholder.typicode.com"
"""REST API url"""


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            usr_id = int(sys.argv[1])
            users = requests.get('{}/users/{}'.format(ENDPOINT, usr_id)).json()
            tds = requests.get('{}/todos'.format(ENDPOINT)).json()
            usr_name = users.get('username')
            todos = list(filter(lambda x: x.get('userId') == usr_id, tds))
            with open("{}.json".format(usr_id), 'w') as json_file:
                results = list(map(
                    lambda x: {
                        "task": x.get("title"),
                        "completed": x.get("completed"),
                        "username": usr_name
                    },
                    todos
                ))
                results = {
                    "{}".format(usr_id): results
                }
                json.dump(results, json_file)
