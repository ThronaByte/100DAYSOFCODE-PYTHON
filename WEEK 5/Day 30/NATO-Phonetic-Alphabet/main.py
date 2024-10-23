# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def phonetic_code():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, word not available")
        phonetic_code()
    else:
        print(output_list)
phonetic_code()

# is_correct = messagebox.askokcancel(title=website_name, message=f"There are the details entered: \nWebsite: {website_name} "
#                                                    f"\nEmail: {email_name} "
#                                                    f"\nPassword: {mypass_name}")

# if is_correct: