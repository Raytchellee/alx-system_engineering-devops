#!/usr/bin/python3
"""returns file injson format"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    id = argv[1]
    link = "https://jsonplaceholder.typicode.com/"
    person = requests.get(link + "users/{}".format(id)).json()
    name = person.get("username")
    tasks = requests.get(link + "todos", params={"userId": id}).json()

    with open("{}.json".format(id), "w") as f:
        json.dump({id: [{
                "username": name,
                "task": idx.get("title"),
                "completed": idx.get("completed")
            } for idx in tasks]}, f)
