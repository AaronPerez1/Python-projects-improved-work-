import random 

players_action = input("rock, paper or scissors: ")
actions_possible = ["rock", "paper", "scissors"]
computer_action = random.choice(actions_possible)
print("You chose {players_action}, computer chose {computer_action}.")

if players_action == computer_action:
    print("Both players selected {players_action}. It's a tie!")
elif players_action == "rock":
    if computer_action == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif players_action == "paper":
    if computer_action == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif players_action == "scissors":
    if computer_action == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")