from typing import Tuple


opponent_hand_dict = dict(rock="A", paper="B", scissors="C")
my_hand = dict(rock="X", paper="Y", scissors="Z")


LOSE_VALUE = 0
DRAW_VALUE = 3
WIN_VALUE = 6

LOSE_LETTER = 'X'
WIN_LETTER = 'Z'
DRAW_LETTER = 'Y'

SCISSORS_NUMBER_VALUE = 3
ROCK_NUMBER_VALUE = 1
PAPER_NUMBER_VALUE = 2

def get_hand_score(hand: str):
    if hand == my_hand["rock"]:
        return 1
    elif hand == my_hand["paper"]:
        return 2
    else:
        return 3  # scissors


def get_hand_from_outcome_and_opponent(opponent_hand: str, choice: str) -> Tuple[int,int]:

    # DRAW 
    # - return the value of the same hand
    if choice == DRAW_LETTER:
        if opponent_hand == opponent_hand_dict['rock']:
            return (ROCK_NUMBER_VALUE,DRAW_VALUE)
        elif opponent_hand == opponent_hand_dict['paper']:
            return (PAPER_NUMBER_VALUE,DRAW_VALUE)
        else:
            return (SCISSORS_NUMBER_VALUE,DRAW_VALUE)
    
    # LOSE
    # - return the value of the losing hand
    if choice == LOSE_LETTER:
        if opponent_hand == opponent_hand_dict['rock']:
            return (SCISSORS_NUMBER_VALUE,LOSE_VALUE)
        elif opponent_hand == opponent_hand_dict['paper']:
            return (ROCK_NUMBER_VALUE,LOSE_VALUE)
        else:
            return (PAPER_NUMBER_VALUE,LOSE_VALUE)
        
    # WIN
    # - return the value of the winning hand
    if opponent_hand == opponent_hand_dict['rock']:
        return (PAPER_NUMBER_VALUE,WIN_VALUE)
    elif opponent_hand == opponent_hand_dict['paper']:
        return (SCISSORS_NUMBER_VALUE,WIN_VALUE)
    else:
        return (ROCK_NUMBER_VALUE,WIN_VALUE)


def main():

    # Open the file, and get all the calories
    with open("data.txt", "r") as file:
        scores = []
        for line in file:
            opponent_choice, my_choice = line.split(" ")
            opponent_choice = opponent_choice.strip()
            my_choice = my_choice.strip()

            single_round = get_hand_from_outcome_and_opponent(opponent_choice, my_choice)

            scores.append(sum(single_round))
        print(sum(scores))


if __name__ == "__main__":
    main()
