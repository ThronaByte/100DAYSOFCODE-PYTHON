from auction_art import logo
import os 
print(logo)
def cls():
    os.system('cls')#for windows
def clear():
    os.system('clear') #'for mac or linux'
auction = {}

def highest_bid(auction):
    score = 0
    name = ""
    for auc in auction:
        price = auction[auc]
        if price > score:
            score = auction[auc]
            price =  score
            name = auc
    print(f"The Highest Bidder is '{name}' with the price of '{score}'")
    
ask = True
while ask:
    name = input("What is your name? ").lower()   
    bid_price = int(input(f"'{name}' what is your bidding price? "))
    auction[name] = bid_price
    other_users = input("Are there any other users who want to bid? 'yes' or 'no': ").lower()
    if other_users == 'yes':
        cls()#for windows
        # clear()#for mac or linux
    else:
        ask = False
        highest_bid(auction=auction)
        
