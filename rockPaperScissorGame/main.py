import random

while True:
    choices = ["rock", "paper", "scissor"]

    computer = random.choice(choices)
    player = None
    while player not in choices:
        player = input("rock, paper, or scissor?: ").lower()

    print("computer: " + computer)
    print("player: " + player)

    if player == computer:
        print("Tie!")
    elif player == "rock":
        if computer == "scissor":
            print("You win!")
        else:
            print("You lose!")
    elif player == "paper":
        if computer == "rock":
            print("You win!")
        else:
            print("You lose!")
    elif player == "scissor":
        if computer == "paper":
            print("You win!")
        else:
            print("You lose!")
    play_again = input("Play again? (yes/no): ".lower())

    if play_again != "yes":
        break
print("Bye")