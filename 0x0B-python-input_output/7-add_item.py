#!/usr/bin/python3

import json
import sys
import os

if os.path.isfile("add_item.json"):
    with open("add_item.json", mode="r+", encoding="UTF8") as textfile:
        list1 = json.load(textfile)
    args = list(sys.argv)
    for i in range(1, len(args)):
        list1.append(args[i])
    with open("add_item.json", mode="w", encoding="UTF8") as textfile:
        textfile.write(json.dumps(list1))
else:
    with open("add_item.json", mode="w+", encoding="UTF8") as textfile:
        textfile.write(json.dumps(list1))
