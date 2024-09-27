# Leap year Excercise
year = int(input("which year do you wnat to check: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('it a leap year')
        else:
            print('not a leap year')
    else:
       print('it a leap yea') 
else:
    print('not a leap')
    