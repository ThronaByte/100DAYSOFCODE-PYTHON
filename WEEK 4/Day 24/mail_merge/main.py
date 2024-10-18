with open('./Input/Names/invited_names.txt') as name:
    names = (name.readlines())

with open('./Input/Letters/starting_letter.txt') as letter:
    content = letter.read()
    for name in names:
        name = name.strip()
        new = content.replace("[name]", name)
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode='w') as send:
            send.write(new)
