def main():
    highest_calorie_count = 0
    # Open the file, and get all the calories
    with open("data.txt", "r") as file:
        current_calorie_count = 0
        for line in file:
            if line == "\n":
                if current_calorie_count > highest_calorie_count:
                    highest_calorie_count = current_calorie_count
                current_calorie_count = 0
            else:
                current_calorie_count += int(line)

    print("highest calorie count: ", highest_calorie_count)


if __name__ == "__main__":
    main()
