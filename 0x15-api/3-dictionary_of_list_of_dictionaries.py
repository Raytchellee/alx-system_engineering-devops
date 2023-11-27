#!/usr/bin/python3
"""returns file injson format"""
import json
import requests

if __name__ == "__main__":
    link = 'https://jsonplaceholder.typicode.com/'
    person = requests.get(link + "users").json()

    with open("todo_all_employees.json", mode="w", newline="") as f:
        json.dump({
            itm.get("id"): [{
                "username": itm.get("username"),
                "completed": idx.get("completed"),
                "task": idx.get("title")
            } for idx in requests.get(link + "todos",
                                      params={"userId": itm.get("id")}).json()]
            for itm in person}, f)
