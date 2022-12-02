opponent_hand = dict(rock="A", paper="B", scissors="C")
my_hand = dict(rock="X", paper="Y", scissors="Z")

LOST_VALUE = 0
DRAW_VALUE = 3
WIN_VALUE = 6


def get_hand_score(hand: str):
    if hand == my_hand["rock"]:
        return 1
    elif hand == my_hand["paper"]:
        return 2
    else:
        return 3  # scissors


def get_single_round_winner(opponent_choice: str, my_choice: str) -> int:

    if opponent_choice == opponent_hand["rock"]:
        if my_choice == my_hand["rock"]:
            return DRAW_VALUE
        elif my_choice == my_hand["paper"]:
            return WIN_VALUE
        else:  # my choice is scissors
            return LOST_VALUE

    if opponent_choice == opponent_hand["paper"]:
        if my_choice == my_hand["rock"]:
            return LOST_VALUE
        elif my_choice == my_hand["paper"]:
            return DRAW_VALUE
        else:  # my choice is scissors
            return WIN_VALUE

    # scissors case
    if my_choice == my_hand["rock"]:
        return WIN_VALUE
    elif my_choice == my_hand["paper"]:
        return LOST_VALUE
    else:  # my choice is scissors
        return DRAW_VALUE


def main():

    # Open the file, and get all the calories
    with open("data.txt", "r") as file:
        scores = []
        for line in file:
            opponent_choice, my_choice = line.split(" ")
            opponent_choice = opponent_choice.strip()
            my_choice = my_choice.strip()

            single_round = get_single_round_winner(opponent_choice, my_choice)
            hand_score = get_hand_score(my_choice)

            round_total = single_round + hand_score
            scores.append(round_total)
        print(sum(scores))


if __name__ == "__main__":
    main()
