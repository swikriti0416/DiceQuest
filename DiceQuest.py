import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll

value = roll()

# Loop to get the number of players between 2 and 4
while True:
    player = input("Enter the number of players (2-4): ")
    if player.isdigit():
        player = int(player)
        if 2 <= player <= 4:
            break
        else:
            print("Must be between 2-4 players.")
    else:
        print("Invalid input, try again.")

max_score = 30
player_score = [0 for _ in range(player)]

print(player_score)

# Main game loop
while max(player_score) < max_score:
    for player_idx in range(player):
        print("Player", player_idx + 1, "turn has just started!")
        print("Your total score is:", player_score[player_idx], "\n")

        current_score = 0

        # Loop for each player's turn
        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1. Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:", value)
                print("Your score is:", current_score)

        player_score[player_idx] += current_score
        print("Your Total score is:", player_score[player_idx], "\n")

# Determine the winner
max_score = max(player_score)
winning_idx = player_score.index(max_score)
print("Player number", winning_idx + 1, "is the winner with the score of:", max_score)
