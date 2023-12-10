import random

roll = random.randint(1,6)

guess = int(input("Guess the dice roll:\n"))

if guess == roll:
    print("WIN! They rolled a " + str(roll))
else:
    print("Computer roll " + str(roll)+ ", Not this time :(")