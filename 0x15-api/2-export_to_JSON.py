#!/usr/bin/python3
""" Python script to export data in the JSON format """
import csv
import json
import requests as re
rom sys import argv


if __name__ == '__main__':

    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/users"
    user = re.get(url + '/{}'.format(user_id)).json()
    todo = re.get(url + '/{}/todos'.format(user_id)).json()

    task_list = []

    for task in todo:
        task_dict = {}
        task_dict['task'] = task.get('title')
        task_dict['completed'] = task.get('completed')
        task_dict['username'] = user.get('username')
        task_list.append(task_dict)

    task_obj = {}

    task_obj[user_id] = task_list
    with open("{}.json".format(user_id), 'w') as jsfile:
        json.dump(task_obj, jsfile)
