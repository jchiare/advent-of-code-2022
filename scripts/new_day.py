# /usr/bin/python3
import os
import sys

day_number = sys.argv[1]
folder = f"day{day_number}"

os.mkdir(folder)

task_one_file = open(f"{folder}/task_one.py", "w")
task_two_file = open(f"{folder}/task_two.py", "w")
data_file = open(f"{folder}/data.txt", "w")
