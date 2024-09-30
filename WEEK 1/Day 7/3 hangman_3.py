# Welcome to the Hangman Game 
import random
word_list = ["apple", "baboon", "camel"]
chosen_word = random.choice(word_list)

# Useer 
print(f"Useeeer, the solution is {chosen_word}")
display = []
    
for each in chosen_word:
    display += "_"
print(display)
while True:
    guess = input("Guess a letter: ").lower()
    for f in range(len(chosen_word)):
        if chosen_word[f] in guess:
            display[f] = chosen_word[f]
    
    print(display)
    if '_' not in display:
        False
        print("Congratulation,  you've completed the challege")
        break