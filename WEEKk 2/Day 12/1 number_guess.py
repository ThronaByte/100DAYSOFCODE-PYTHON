import random

EASY = 10
MEDIUM = 7
HARD = 5

def type():
    player = input("Enter difficulty (type 'easy', 'medium', or 'hard'): ").lower()

    if player == "hard":
        return HARD
    elif player == "medium":
        return MEDIUM 
    elif player == "easy":
        return EASY 
    else:
        return "Invalid input"
    
def compare_guess(player_guess, answer, turns):
    if player_guess < answer:
        print("Too low")
        return turns -1 
    elif player_guess > answer:
        print("Too high")
        return turns - 1
    else:
        print( f"You got it the answer was: {answer} 🌹🏆💻")
   
def number_guess():
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1,100)
    print(answer)
    
    level = type()
    number = level #this line is to check the (level variable number) against the (constant)
    
    player_guess = 0
    while player_guess != answer:
        print(f"You have {level}/{number} lives left.")

        player_guess = int(input("Make a guess: "))
        
        level = compare_guess(player_guess, answer, level)
        if level == 0:
            print("Game ended\nYou were unable to guess the right number.")
            return
        elif level == 1:
            print("\nYou have one(1) more chance left...")
            
number_guess()