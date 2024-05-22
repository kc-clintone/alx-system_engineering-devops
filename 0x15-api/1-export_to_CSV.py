#!/usr/bin/python3
"""
gathers data from API and exports it to CSV file
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
            usr_name = users.get('username')
            todos = list(filter(lambda x: x.get('userId') == id, tds))
            with open('{}.csv'.format(usr_id), 'w') as file:
                for t in todos:
                    file.write(
                        '"{}","{}","{}","{}"\n'.format(
                            usr_id,
                            usr_name,
                            t.get('completed'),
                            t.get('title')
                        )
                    )
