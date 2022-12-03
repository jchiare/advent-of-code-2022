import os


def get_priority(letter: str) -> int:
    char_point = ord(letter)

    if char_point >= 97:  # lower case
        return char_point - 96
    return char_point - 65 + 27  # uppercase


def main():

    cwd = os.getcwd()
    with open(os.path.join(cwd, "data.txt"), "r") as file:

        matching_rucksack_characters = list()
        file_as_list = file.readlines()
        for i in range(0, len(file_as_list), 3):
            stripped_rucksacks = [s.strip() for s in file_as_list[i : i + 3]]
            first_rucksack = set(stripped_rucksacks[0])
            second_rucksack = set(stripped_rucksacks[1])

            searched_chars = set()
            for char in stripped_rucksacks[2]:
                if char not in searched_chars:
                    priority = get_priority(char)
                    if char in first_rucksack and char in second_rucksack:
                        matching_rucksack_characters.append(priority)
                    searched_chars.add(char)

        print(sum(matching_rucksack_characters))


if __name__ == "__main__":
    main()
