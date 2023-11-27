#!/usr/bin/python3
"""returns todos in csv format"""
import csv
import requests
from sys import argv

if __name__ == "__main__":
    uid = argv[1]

    link = "https://jsonplaceholder.typicode.com/"
    person = requests.get(link + "users/{}".format(uid)).json()

    name = person.get("username")
    tasks = requests.get(link + "todos", params={"userId": uid}).json()

    with open("{}.csv".format(uid), "w", newline="") as f:
        r_w = csv.writer(f, quoting=csv.QUOTE_ALL)

        [r_w.writerow(
            [uid, name, idx.get("completed"), idx.get("title")]
         ) for idx in tasks]
