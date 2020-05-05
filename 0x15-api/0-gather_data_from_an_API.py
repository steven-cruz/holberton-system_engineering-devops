#!/usr/bin/python3
"""
    Python script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress.
"""
import requests as re
from sys import argv


if __name__ == '__main__':

    user_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users'
    user = re.get(url + '/{}'.format(user_id)).json()
    todo = re.get(url + '/{}/todos'.format(user_id)).json()
    complete = []

    for task in todo:
        if task.get('completed') is True:
            complete.append(task.get('title'))

    print('Employee {} is done with tasks({}/{}):'.format
          (user.get('name'), len(complete), len(todo)))

    for task in complete:
        print('\t {}'.format(task))
