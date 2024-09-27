# Head or Tails Excercise
import random 
user  = int(input("create a seed number: "))
random.seed(user)
rand = random.randint(0,1)
if rand == 1:
    print('Tails')
else:
    print('Head')