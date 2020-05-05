#!/usr/bin/python3
""" Python script to export data in the JSON format """
import csv
import json
import requests as re
from sys import argv


if __name__ == '__main__':

    user = re.get('https://jsonplaceholder.typicode.com/users').json()
    user_dict = {}
    us_dict = {}

    for us in user:
        user_id = us.get('id')
        user_dict[user_id] = []
        us_dict[user_id] = us.get('username')

    todo = re.get('https://jsonplaceholder.typicode.com/todos').json()

    for task in todo:
        task_dict = {}
        user_id = task.get('userId')
        task_dict['username'] = us_dict.get(user_id)
        task_dict['task'] = task.get('title')
        task_dict['completed'] = task.get('completed')
        user_dict.get(user_id).append(task_dict)

    with open('todo_all_employees.json', 'w') as jsfile:
        json.dump(user_dict, jsfile)
