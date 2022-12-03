# /usr/bin/python3
import os
import sys

day_number = sys.argv[1]
folder = f"day{day_number}"

os.mkdir(folder)

BASE_TASK_PYTHON_CODE = """
import os 

def main():

    cwd = os.getcwd()
    with open(os.path.join(cwd, "data.txt"), "r") as file:
        for line in file:
            # do something

if __name__ == "__main__":
    main()
"""

task_one_file = open(f"{folder}/task_one.py", "w")
task_two_file = open(f"{folder}/task_two.py", "w")
data_file = open(f"{folder}/data.txt", "w")

task_one_file.write(BASE_TASK_PYTHON_CODE)
task_two_file.write(BASE_TASK_PYTHON_CODE)

task_one_file.close()
task_two_file.close()
data_file.close()

