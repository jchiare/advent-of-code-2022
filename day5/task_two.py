import sys
import re


def main():

    use_sample_data = sys.argv[1] if len(sys.argv) > 1 else None
    data_file = "data.txt" if not use_sample_data else "sample-data.txt"

    with open(data_file, "r") as file:
        count = 0
        array = []
        for line in file:
            count += 1
            if "move" in line:
                pattern = re.compile(r"\d+")
                [first, second, third] = pattern.finditer(line)
                amount_to_move = int(first.group())
                array_index_to_move_from = int(second.group()) - 1
                array_index_to_move_to = int(third.group()) - 1

                array[array_index_to_move_to] = (
                    array[array_index_to_move_from][0:amount_to_move]
                    + array[array_index_to_move_to]
                )
                array[array_index_to_move_from] = array[array_index_to_move_from][
                    amount_to_move:
                ]
            elif any(char.isdigit() for char in line):
                # do nothing
                pass
            else:
                space_count = 0
                # create array to hold letters if it's empty
                if len(array) == 0:
                    line_length = round(len(line) / 4)
                    for i in range(0, line_length):
                        array.append([])
                for i in range(0, len(line), 4):
                    item = line[i + 1 : i + 2]
                    if item.isalpha():
                        array[space_count].append(line[i + 1 : i + 2])
                    space_count += 1
        word = ""
        for sub_array in array:
            word += sub_array[0]
        print(word)


if __name__ == "__main__":
    main()
