#!/usr/bin/python3
"""
returns info about employee TODO progress
Implemented using recursion
"""
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
            usr_name = users.get('name')
            todos = list(filter(lambda x: x.get('userId') == id, tds))
            resolved = list(filter(lambda x: x.get('completed'), todos))
            print(
                'Employee {} is done with tasks({}/{}):'.format(
                    usr_name,
                    len(resolved),
                    len(todos)
                )
            )
            for k in resolved:
                print('\t {}'.format(k.get('title')))
