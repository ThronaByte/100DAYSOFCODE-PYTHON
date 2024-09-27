"""

rock wins against scissors
scissors wins against paper
papers wins against rock

"""
import random
print("Welcome to the 'RPS' game")
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

gamee = ["Rock", "Paper", "Scissors"]
computer = random.randint(0, len(gamee)-1)
print(f"You chose: {gamee[user]}")
print(f"Computer chose: {gamee[computer]}")

if user == 0 and computer == 0:
    print("Draw")
elif user == 1 and computer == 1:
    print("Draw")
elif user == 2 and computer == 2:
    print("Draw")
elif computer == 0 and user == 2:
    print(f"computer chose {gamee}: \nYou lose")
elif computer == 2 and user == 1:
    print(f"computer chose {gamee}: \nYou lose")
elif computer == 1 and user == 0:
    print(f"computer chose {gamee}: \nYou lose")
elif user == 1 and computer == 0:
    print('You win')
elif user == 2 and computer == 1:
    print('You win')
elif user == 0 and computer == 2:
    print('You win')
else:
    print('invalid input')
