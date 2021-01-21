#!/usr/bin/python3

import json
import sys

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

if __name__ == '__main__':
    list1 = []

    try:
        list1 = load_from_json_file("add_item.json")
    except Exception:
        save_to_json_file(list1, "add_item.json")

    args = list(sys.argv)

    for i in range(1, len(args)):
        list1.append(args[i])

    save_to_json_file(list1, "add_item.json")
