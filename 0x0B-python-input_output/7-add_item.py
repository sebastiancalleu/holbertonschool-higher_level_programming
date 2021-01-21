#!/usr/bin/python3


import sys

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

if __name__ == '__main__':
    try:
        list1 = load_from_json_file("add_item.json")
        list1 += sys.argv[1:]
        save_to_json_file(list(list1), "add_item.json")
    except Exception:
        save_to_json_file(list(sys.argv[1:]), "add_item.json")


