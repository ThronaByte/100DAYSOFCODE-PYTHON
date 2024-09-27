# Who will pay the bill
import random
print("\nWelcome to who is paying")
user_seed = int(input("enter a seed number: "))
random.seed(user_seed)

individual_person = input("enter all the name's of person seperated by comma. ").upper()
spliting = individual_person.split(',')

getting_person = random.randint(0, len(spliting)-1)

print(getting_person)
who_is_paying = spliting[getting_person]
print(f"'{who_is_paying}' is paying for all the bill!💳💸")