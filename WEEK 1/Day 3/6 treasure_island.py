# Treasure island
print("Welcome to Treasure Island \nYour mission is to find the treasure")
move = input("'left' OR 'right'? \n").lower()
if move == 'left':
    move2 = input("'swim' OR 'wait'? \n").lower()
    if move2 == 'wait':
        door = input("Which door are you entering 'Red', 'Blue' or 'Yellow'? \n").lower()
        if door == 'yellow':
            print('You Found the Treasure. Congratulations 💻🖱💻')
        else:
            print('You entered the wrong door. Game Over🎮🎮')
    else:
        print('You entered a room full of women💃💃💃. Game over')
else:
    print('You\'ve entered the wrong house🏠. Game over')
    
print("\nSee you tommorow🕑🕑. Bye...👋🙋‍♂️")