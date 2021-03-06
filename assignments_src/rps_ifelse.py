"""
use a loop to play 7 consecutive games of RPS and determine winner using
only if/elif/else statements

"""
games = 7
invalid = 0
play = True
p1winner = 0
p2winner = 0
ties = 0

while play:
    # save valid options
    valid = ["rock", "paper", "scissors"]
    # get player inputs
    p1 = input("Player 1: please enter your play: ")
    if p1 == valid[0] or p1 == valid[1] or p1 == valid[2]:
        # valid game: move to player 2
        p2 = input("Player 2: please enter your play: ")
        if p2 == valid[0] or p2 == valid[1] or p2 == valid[2]:
            # valid game- check for winner
            if p1 == p2:
                ties += 1
                print("It's a tie!")
            elif p1 == "paper":
                if p2 == "rock":
                    print("Paper cover's rock!")
                    p1winner += 1
                else:  # scissors
                    print("Scissors cut paper!")
                    p2winner += 1
            elif p1 == "rock":
                if p2 == "paper":
                    print("Paper cover's rock!")
                    p2winner += 1
                else:  #scissors
                    print("Rock smashes scissors!")
                    p1winner += 1
            else:  # scissors
                if p2 == "rock":
                    print("Rock smashes scissors!")
                    p2winner += 1
                else: #paper
                    print("Scissors cut paper!")
                    p1winner += 1
            # decrement gamecount
            games += - 1
            if games == 0:
                play = False  # stop after 7 total games (including invalid)
        else:
            print("Player 2 entered invalid play")
            invalid += 1
            games += -1
            # restart game
            continue
    else:
        print("Player 1 entered invalid play")
        # restart game
        invalid += 1
        games += -1
        continue

print(f"Player 1 won: {p1winner} games, player 2 won: {p2winner}")
print(f"games, and there were {ties} ties. There were a total of ")
print(f"{invalid} invalid games.")




