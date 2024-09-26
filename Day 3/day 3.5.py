# Love Calculator to check if your crush love's you 😏😏
print('Welcome to the love calculator')
name1 = input("what is your name? \n").lower()
name2 = input("what is their name? \n").lower()

combined_name = name1 + name2
print(combined_name)
T = combined_name.count('t')
R = combined_name.count('r')
U = combined_name.count('u')
E = combined_name.count('e')
crush1 = T+R+U+E

L = combined_name.count('l')
O = combined_name.count('o')
V = combined_name.count('v')
E = combined_name.count('e')
crush2 = L+O+V+E

lovescore = int(str(crush1) + str(crush2))
print(lovescore)
if lovescore < 10 or lovescore > 90:
    print(f'Your score is {lovescore}, you go together like coke and mentos.')
elif lovescore >= 40 and lovescore <= 50:
    print(f'Your score is {lovescore}, you are alrigt together.')
else:
    print(f'Your score is {lovescore}')