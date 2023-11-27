#!/usr/bin/python3
"""gets info by id"""
import requests
from sys import argv

if __name__ == "__main__":
    link = "https://jsonplaceholder.typicode.com/"
    person = requests.get(link + "users/{}".format(argv[1])).json()
    tasks = requests.get(link + "todos", params={"userId": argv[1]}).json()

    done = [i.get("title") for i in tasks if i.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        person.get("name"), len(done), len(tasks)))
    [print("\t {}".format(idx)) for idx in done]
