#!/usr/bin/python3
"""import api from a url"""
import requests
import sys

if __name__ == "__main__":
    try:
        id = int(sys.argv[1])
        url = "https://jsonplaceholder.typicode.com/"
        res = requests.get("{}/users/{}".format(url, id)).json()
        print(res)
        res_todo = requests.get("{}/todos".format(url),
                                params={"userId": id}).json()
        task_comp = [t.get('title') for t in res_todo if t.completed]
        user = res.get('name')
        b = "Employee {} is done with tasks({}/{}):".format(
            user, len(task_comp), len(res_todo))
        print(b)
        for t in task_comp:
            print("\t {}".format(t))
    except ValueError:
        pass
