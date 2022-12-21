import re
import sys
from typing import List, Dict 

def find_file_or_directory(needle : str, haystack: List[Dict[str,any]]):
    needle_list = [needle_dict for needle_dict in haystack if needle_dict['name'] == needle ]
    result = needle_list[0] if len(needle_list) > 0 else None
    return result

def main():

    use_sample_data = sys.argv[1] if len(sys.argv) > 1 else None
    data_file = "data.txt" if not use_sample_data else "sample-data.txt"

    with open(data_file, "r") as file:
        filesystem = []
        previous_location = None
        current_location = None
        for line in file:
            line = line.strip('\n')
            if line[0] == '$': # user command
                if line[2:4] == 'cd':
                    # cd /
                    if line[5:7] == '..':
                        file_or_dir_dict = find_file_or_directory(previous_location,filesystem)
                        current_location = file_or_dir_dict['name']
                    # cd $dir
                    else:
                        previous_location = current_location
                        current_location = line[5:]
                        filesystem.append({'name': current_location, 'type': 'directory','contents': [], 'sub_directory': previous_location})
                elif line[2:4] == 'ls':
                    pass
            else: # output of ls command
                # file
                current_dir = find_file_or_directory(current_location, filesystem)
                if line[0].isdigit():
                    # digits_list = re.findall(r'\d', line)
                    # digits = ''.join(digits_list)
                    current_dir['contents'].append(line)
                else: # directory
                    current_dir['contents'].append(line)
        print('filesystem: ', filesystem)
        
                
                

if __name__ == "__main__":
    main()
