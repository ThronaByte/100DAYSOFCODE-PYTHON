# compare A
# vs
# against B 
# which site is mostly visited? Type "a" or "b"
# if they g0t it right 
# print(you're right! Current score "..."
# they should keep playing with the current answer:  until they misses and give them their score

from hla import logo, o_r, starts
from list_of_website import data
from random import choice
import os
def clear():
    os.system('cls')

clear()
def get_random_website(data):
    web_1 = choice(data)
    web_2 = choice(data)
    return web_1,web_2

def web_data(website):
    website_name = website['name']
    website_description = website['description']
    website_country = website['country']
    return f"{website_name}, a {website_description}, in {website_country}"

def visit_count(website):
    website_name = website['name']
    website_visit = website['visit_count']
    return f"{website_name} has {website_visit} visits!"
    
    
def compare(guess, website1, website2):
    if website1 > website2:
        return guess == "A"
    else:
        return guess == "B"

def higher_lower():
    
    print(logo)
    score = 0
    higher_lower = True
    website2 = choice(data)
    while higher_lower:
        website1 =website2
        website2 = choice(data)

        if website1 == website2:
            website2 = choice(data)
            
        print(f"compare A: {web_data(website=website1)}")
        print(o_r)
        print(f"Against B: {web_data(website=website2)}")
        
        guess = input('Type "A" or "B": ').upper()
        while guess not in ['A','B']:
            guess = input('Invalid choice! Type "A" or "B": ').upper()


        visit_count_1 = website1['visit_count']
        visit_count_2 = website2['visit_count']
        answer = compare(guess=guess, website1=visit_count_1, website2=visit_count_2)
        
        clear()
        print(logo)
        if answer:
            score +=1
            print(f"You're right! Current score: {score}") 
            print(f"{visit_count(website=website1)} while {visit_count(website=website2)}")
        else:
            higher_lower = False
            print(f"Incorrect! Your score is: {score}")
            print(f"{visit_count(website=website2)} while {visit_count(website=website1)}")
            
    if higher_lower == False:
        play_again = input("\nPress 'P' to play again. ")
        if play_again == "P":
            return higher_lower()
        while play_again not in ['P']:
            play_again = input('Invalid choice! Press "P" to play again.: ').upper()
        clear()
        
def start():
    while True:
        print(starts)
        print("Guess which website is the most visited on the internet each month.\nA game of higher or lower using websites monthly visits stats.")
        choice = input("Press 'P' to play. ").upper()
        if choice == 'P':
            clear()
            higher_lower()
        else:
            while choice not in ["P"]:
                choice = input("Invalid choice! Press 'P' to play. ").upper()

start()