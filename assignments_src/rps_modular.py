"""
Winner of the game will be determined by arithmetic and modular math
come up with a small formula which are the winner
simulate 10 games
"""
games = 10
p1invalid = 0
p2invalid = 0
p1winner = 0
p2winner = 0
ties = 0
play = True

while games > 0:
    # save valid options
    valid = ["rock", "paper", "scissors"]
    # get player inputs
    p1 = input("Player 1: please enter your play: ")
    if p1 == valid[0]:
        p1 = 1
    elif p1 == valid[1]:
        p1 = 2
    elif p1 == valid[2]:
        p1 = 3
    else:
        print("Player 1 entered invalid play")
        # restart game
        p1invalid += 1
        continue

    # valid: move to player 2
    turn = True
    while turn:
        p2 = input("Player 2: please enter your play: ")
        if p2 == valid[0]:
            p2 = 1
            turn = False
        elif p2 == valid[1]:
            p2 = 2
            turn = False
        elif p2 == valid[2]:
            p2 = 3
            turn = False
        else:
            print("Player 2 entered invalid play")
            p2invalid += 1
            # keep prompting p2

    # valid game- check for winner
    if p1 - p2 == 0:
        ties += 1
        print("It's a tie!")
    elif p1 - p2 < 0:
        # p1 is rock OR p1 is paper and p2 scissors
        if p1 % p2 == 2:
            # p1 is paper and p2 scissors
            print("Scissors cut paper!")
            p2winner += 1
        # p1 is rock
        elif 4 % p2:
            # reaches this if not = 0, meaning p2 is scissors
            print("Rock smashes scissors!")
            p1winner += 1
        else:
            # p2 is paper
            print("Paper cover's rock!")
            p2winner += 1
    else :
        # either p2 is rock or p2 is paper and p1 scissors
        if p2 % p1 == 2:
            # p2 paper and p1 scissors
            print("Scissors cut paper!")
            p1winner += 1
        # p2 is rock
        elif 4 % p1:
            # reaches this if not = 0, meaning p1 is scissors
            print("Rock smashes scissors!")
            p2winner += 1
        else:
            # p1 is paper
            print("Paper cover's rock!")
            p1winner += 1

    # decrement gamecount
    games += - 1
    if games == 0:
        play = False  # stop after 10 valid games


print(f"Player 1 won: {p1winner} games, player 2 won: {p2winner}")
print(f"games, and there were {ties} ties. Player 1 made {p1invalid}  gestures")
print(f"and Player 2 made {p2invalid} invalid gestures.")

