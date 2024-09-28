# Py password generator
import random
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', ';', ':', '"', ',', '.', '<', '>', '?', '`', '~']

print("\nWelcome to the PyPassword Generator!")

ur_alphabet = int(input("How many letter would you like in your password? \n "))
ur_number = int(input("How many numbers would you like?\n "))
ur_symbol =  int(input("How many symbols would you like?\n "))
#

pass_list = []
for pl in range(1, ur_symbol +1):
    pass_list.append(random.choice(symbols))
for pl in range(1, ur_number + 1):
    pass_list.append(random.choice(numbers))
for pl in range(1, ur_alphabet +1):
    pass_list.append(random.choice(alphabets))
    
# print(pass_list)
random.shuffle(pass_list)

pass_word = ''
for pw in pass_list:
    pass_word += str(pw)

# print(password)
print(f"Here is your password: {pass_word}")
