import random
import os
from black_jack_art import logo
def clear():
    os.system('cls')

def deal_card():
    """All Black Jack numbers in the card"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return  card


def calculate_score(cards):
    """Returns the score of the cards"""
    score  = sum(cards)
    if score == 21 and len(cards) ==2:
        return 0
    if 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)
    return score

def compare(user_score, computer_score):
    """Comparing user and computer score"""
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"

    if user_score == computer_score:
        return "Draw 📍"
    elif computer_score == 0:
        return "You lose 😢"
    elif user_score == 0:
        return "You win 🏆"
    elif user_score >21:
        return "You lose"
    elif computer_score >21:
        return "You win"
    elif computer_score > user_score:
        return "You lose"
    else:
        return "You win"
    

def black_jack():
    """Welcome To The Black Jack Game"""
    print(logo)
    user_cards = []
    computer_cards = []
    game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
        
    while not game_over:
            
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your card: {user_cards}, current score {user_score}")
        print(f"Computer first card: {computer_cards[0]}")

        if user_score and computer_score == 0 or user_score > 21:
            game_over = True
        else:
            game_not_ended = input("Type 'h' to Hit 's' to Stand: ").lower()
            if game_not_ended == 'h':
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

    play_again = input("Type 'r' to restart the game or 'q' to quit playing: ").lower()
    if play_again == 'r':
        clear()
        black_jack()
    else:
        game_over = True
black_jack()
