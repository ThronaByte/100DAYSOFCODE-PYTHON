# Welcome to the Hangman Game 
import random
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

guess = input("Guess a letter: ").lower()
for f in chosen_word:    
    if guess in f:
        print("right")
    else:
        print("wrong")
print(chosen_word)