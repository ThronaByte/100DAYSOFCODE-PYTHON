# The Rollercoaster Game

print('\nWelcome to the rollercoaster game')
height = int(input('What is your height? '))

bill = 0
if height > 120:
    age = int(input('How old are you? '))
    if age < 12:
        bill = 5
        print('Child tickets are N5')
    elif age <= 18:
        bill = 7
        print('Youth tickets are N7')
    elif age >= 45 and age <= 55:
        print(f'You have a free ride on us. Your bill is N{bill}')
    else:
        bill = 12
        print('Adult tickets are N12')
        
        # adding bill for photo
    photo = input('Do you want a photo taken? Y or N? ').lower()
    if photo == 'y':
        bill += 5
        print(f'Your bill is N{bill}')
    else:
        print(f'Your bill is N{bill}')
else:
    print('No! you have to grow taller')