# Python Pizza
print("Welcome to Python pizza deliveries")
size = input('what size do you want? S for small, L for large, M for medium: ').lower()
add_pepperoni = input('Do you want pepperoni? Y or N ? ').lower()
extra_cheese = input('Do you want extra cheese? Y or N ? ').lower()

money = 0
if size == 's':
    money +=15
    if add_pepperoni == 'y':
            money += 2
    if extra_cheese == 'y':
        money += 1
        
elif size == 'm':
    money += 20
    if add_pepperoni == 'y':
            money +=3
    if extra_cheese == 'y':
        money += 1
        
elif size == 'l':
    money += 25
    if add_pepperoni == 'y':
            money +=3
    if extra_cheese == 'y':
        money += 1
else:
    print("Invaid input")
            
print(f"Your total bill is: {money}")