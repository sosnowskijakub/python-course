import random

choices = ["rock", "paper", "scissor"]
computer_choice = random.choice(choices)
user_choice = input("Do you want rock, paper or scissor?\n")

if computer_choice == user_choice:
    print("Tie!")
elif user_choice == "rock" and computer_choice == "scissor":
    print("Win! They choose " + computer_choice)
elif user_choice == "paper" and computer_choice == "rock":
    print("Win! They choose " + computer_choice)
elif user_choice == "scissor" and computer_choice == "paper":
    print("Win! They choose " + computer_choice)
else:
    print("You lose! They choose " + computer_choice)