#!/usr/bin/python3
""" Python script that adds all arguments to a Python list
and then saves them to a file"""


import json
import sys
import os.path
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

num_of_args = len(sys.argv)
my_list = []
file_name = "add_item.json"

if (os.path.exists("./add_item.json")) is False:
    save_to_json_file(my_list, file_name)
my_list = load_from_json_file(file_name)
for i in range(1, num_of_args):
    my_list.append(sys.argv[i])
    save_to_json_file(my_list, file_name)
