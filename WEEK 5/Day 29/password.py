#Password Generator Project
import random
def generate_password():

  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
             'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
             'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


  password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]

  symbol = [random.choice(symbols) for _ in range(random.randint(2, 4))]

  number = [random.choice(numbers) for _ in range(random.randint(2, 4))]

  password_list = password_letters + symbol + number

  random.shuffle(password_list)
  my_pass = "".join(password_list)



  print(f"Your password is: {my_pass}")
generate_password()