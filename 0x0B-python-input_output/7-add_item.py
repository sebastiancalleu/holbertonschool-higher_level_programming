#!/usr/bin/python3

import json
import sys

list1 = []

try:
    with open("add_item.json", mode="r+", encoding="UTF8") as textfile:
        list1 = json.load(textfile)
except Exception:
    with open("add_item.json", mode="w+", encoding="UTF8") as textfile:
        textfile.write(json.dumps(list1))

args = list(sys.argv)

for i in range(1, len(args)):
    list1.append(args[i])

with open("add_item.json", mode="w", encoding="UTF8") as textfile:
    textfile.write(json.dumps(list1))
