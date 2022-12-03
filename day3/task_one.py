def get_priority(letter: str) -> int:
    char_point = ord(letter)

    if char_point >= 97:  # lower case
        return char_point - 96
    return char_point - 65 + 27  # uppercase


def main():

    with open("data.txt", "r") as file:

        matching_rucksack_characters = list()
        for line in file:
            line = line.strip()
            half_length_of_rucksack = int(len(line) / 2)
            compartment_one = line[:half_length_of_rucksack]
            compartment_two = line[half_length_of_rucksack:]

            compartment_one_chars = set(compartment_one)

            searched_chars = set()
            for char in compartment_two:
                if char not in searched_chars:
                    priority = get_priority(char)
                    if char in compartment_one_chars:
                        matching_rucksack_characters.append(priority)
                    searched_chars.add(char)

        print(sum(matching_rucksack_characters))


if __name__ == "__main__":
    main()
