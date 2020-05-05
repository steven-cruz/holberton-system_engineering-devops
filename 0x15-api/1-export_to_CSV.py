#!/user/bin/python3
""" Python script to export data in the CSV format """
import csv
import json
import requests as re
from sys import argv


if __name__ == '__main__':

    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/users"
    user = re.get(url + '/{}'.format(user_id)).json()
    todo = re.get(url + '/{}/todos'.format(user_id)).json()

    with open("{}.csv".format(user_id), 'w', newline='') as csvfile:
        fil = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        for task in todo:
            fil.writerow([user_id,
                          user.get('username'),
                          task.get('completed'),
                          task.get('title')])
