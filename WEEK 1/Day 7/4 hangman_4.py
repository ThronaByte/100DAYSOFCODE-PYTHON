import random
print("Welcome to the hangman game")
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lives = 6

word_list = ["apple", "baboon", "camel"]
chosen_word = random.choice(word_list)

print(f"Useeeer, the solution is {chosen_word}")
display = []
    
for each in chosen_word:
    display += "_"
print(display)

while lives > 0:
    guess = input("Guess a letter: ").lower()
    for f in range(len(chosen_word)):
        if chosen_word[f] == guess:
            display[f] = chosen_word[f]

    if guess not in chosen_word:
        lives -=1
        if lives == 0:
            False
            print('You lose')

    print(f"{' '.join(display)}")
    print(stages[lives])
    if '_' not in display:
        False
        print("Congratulation,  you've completed the challege")
        break