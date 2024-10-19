import pandas
data = pandas.read_csv('nato_phonetic_alphabet.csv')
phonetic_data = {row.letter: row.code for (index,row) in data.iterrows()}
# print(phonetic_data)

word = input("Enter a word: ").upper()
names= [phonetic_data[letter] for letter in word]
print(names)
