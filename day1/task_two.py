def main():
    highest_calorie_counts = [0, 0, 0]
    # Open the file, and get all the calories
    with open("data.txt", "r") as file:
        current_calorie_count = 0
        for line in file:

            # each elf's calories are grouped by new lines
            if line == "\n":
                # check if current calorie count is in the top 3
                # if so, add the calorie count to it's respective position
                # and shift all other counts down by own
                if current_calorie_count > highest_calorie_counts[0]:
                    highest_calorie_counts.insert(0, current_calorie_count)
                    highest_calorie_counts.pop()
                elif current_calorie_count > highest_calorie_counts[1]:
                    highest_calorie_counts.insert(1, current_calorie_count)
                    highest_calorie_counts.pop()
                elif current_calorie_count > highest_calorie_counts[2]:
                    highest_calorie_counts.insert(2, current_calorie_count)
                    highest_calorie_counts.pop()

                current_calorie_count = 0
            else:
                current_calorie_count += int(line)

    print(sum(highest_calorie_counts))


if __name__ == "__main__":
    main()
