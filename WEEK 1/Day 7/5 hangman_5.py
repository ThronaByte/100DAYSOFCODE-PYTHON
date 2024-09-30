import random
# import os
from hangman_word import word_list
from hangman_art import logo, stages
print(logo)

lives = 6
chosen_word = random.choice(word_list)
display = []
# clear = os.system('cls')
for each in chosen_word:
    display += "_"
    
print(f"HINT:- The word start with {chosen_word[0]} and end with {chosen_word[-1]}")

while lives > 0:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"letter '{guess}' guessed already.") 
        
    for f in range(len(chosen_word)):
        if chosen_word[f] == guess:
            display[f] = chosen_word[f]

    if guess not in chosen_word:
        print(f"'{guess}' is not in the word")
        lives -=1

    print(f"{' '.join(display)}")
    print(stages[lives])
    if '_' not in display:
        False
        print("Congratulation,  you've completed the challege")
        break
    if lives == 0:
        False
        print(f"\nThe word is '{chosen_word}'")
        print('You lose')
# See you tommorow... Bye